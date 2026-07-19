const fetch = require('node-fetch');

exports.handler = async (event, context) => {
    // Only allow POST
    if (event.httpMethod !== "POST") {
        return { statusCode: 405, body: "Method Not Allowed" };
    }

    try {
        const data = JSON.parse(event.body);

        const { first_name, last_name, email, device_version, issue_type, source_site, message, location } = data;

        // Validate inputs
        if (!first_name || !last_name || !email || !message || !location) {
            return {
                statusCode: 400,
                body: JSON.stringify({ error: "Missing required fields" }),
            };
        }

        const airtableToken = process.env.AIRTABLE_TOKEN;
        const airtableBaseId = process.env.AIRTABLE_BASE_ID;
        const airtableTableName = process.env.AIRTABLE_TABLE_NAME;

        const url = `https://api.airtable.com/v0/${airtableBaseId}/${encodeURIComponent(airtableTableName)}`;

        const fields = {
            "First Name": first_name,
            "Last Name": last_name,
            "Email": email,
            "Message": message,
            "Location": location,
        };

        // Optional fields — only include if provided
        if (device_version) fields["Device / Version"] = device_version;
        if (issue_type) fields["Issue Type"] = issue_type;
        if (source_site) fields["Source Site"] = source_site;

        const response = await fetch(url, {
            method: "POST",
            headers: {
                Authorization: `Bearer ${airtableToken}`,
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                records: [{ fields }],
            }),
        });

        const body = await response.json();

        if (!response.ok) {
            console.error("Airtable Error: ", body);
            return {
                statusCode: response.status,
                body: JSON.stringify({ error: "Failed to submit to Airtable", details: body }),
            };
        }

        return {
            statusCode: 200,
            body: JSON.stringify({ message: "Success" }),
        };
    } catch (error) {
        console.error("Function Error: ", error);
        return {
            statusCode: 500,
            body: JSON.stringify({ error: "Internal Server Error" }),
        };
    }
};

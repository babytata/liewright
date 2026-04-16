const fetch = require('node-fetch');

exports.handler = async (event, context) => {
    // Only allow POST
    if (event.httpMethod !== "POST") {
        return { statusCode: 405, body: "Method Not Allowed" };
    }

    // CORS headers
    const headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type",
    };

    try {
        const data = JSON.parse(event.body);

        const { name, phone, service, message } = data;

        // Validate required fields
        if (!name || !phone || !service || !message) {
            return {
                statusCode: 400,
                headers,
                body: JSON.stringify({ error: "Missing required fields" }),
            };
        }

        const airtableToken = process.env.AIRTABLE_TOKEN;
        const airtableBaseId = process.env.AIRTABLE_BASE_ID;
        // Uses a separate env var so Rooster leads go to their own table
        const airtableTableName = process.env.AIRTABLE_ROOSTER_TABLE || "Rooster Leads";

        const url = `https://api.airtable.com/v0/${airtableBaseId}/${encodeURIComponent(airtableTableName)}`;

        const fields = {
            "Name": name,
            "Phone": phone,
            "Service": service,
            "Message": message,
            "Source": "Rooster Cleaning Website",
            "Date": new Date().toISOString().split('T')[0],
        };

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
                headers,
                body: JSON.stringify({ error: "Failed to submit", details: body }),
            };
        }

        return {
            statusCode: 200,
            headers,
            body: JSON.stringify({ message: "Success" }),
        };
    } catch (error) {
        console.error("Function Error: ", error);
        return {
            statusCode: 500,
            headers,
            body: JSON.stringify({ error: "Internal Server Error" }),
        };
    }
};

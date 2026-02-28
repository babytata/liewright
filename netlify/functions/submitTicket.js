const fetch = require('node-fetch');

exports.handler = async (event, context) => {
    // Only allow POST
    if (event.httpMethod !== "POST") {
        return { statusCode: 405, body: "Method Not Allowed" };
    }

    try {
        const data = JSON.parse(event.body);

        const { name, email, message } = data;

        // Validate inputs
        if (!name || !email || !message) {
            return {
                statusCode: 400,
                body: JSON.stringify({ error: "Missing required fields" }),
            };
        }

        const airtableToken = process.env.AIRTABLE_TOKEN;
        const airtableBaseId = process.env.AIRTABLE_BASE_ID;
        const airtableTableName = process.env.AIRTABLE_TABLE_NAME;

        const url = `https://api.airtable.com/v0/${airtableBaseId}/${encodeURIComponent(airtableTableName)}`;

        const response = await fetch(url, {
            method: "POST",
            headers: {
                Authorization: `Bearer ${airtableToken}`,
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                records: [
                    {
                        fields: {
                            Name: name,
                            Email: email,
                            Message: message,
                            // You can add a 'Status' field like "Todo" if that exists in your table
                            // Status: "Todo",
                        },
                    },
                ],
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

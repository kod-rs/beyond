import { apiCalls } from './comm';

async function addTemperature(portfolio, section, type, value) {
    // let params = { "section": section, "type": type, "portfolio": portfolioName};
    return await apiCalls.handleNewResponse(
        await apiCalls.api.post(
            `temperature/${value}`,
            JSON.stringify({
section, type, 
                portfolio,
            }),
            apiCalls.get_auth_header()
        )
    );

}

async function getAllTemperature(portfolio, section, type) {
console.log("get all temp")
console.log({
    ...apiCalls.get_auth_header(),
    params: {
        portfolio, section, type
    }
    // ...{portfolio, section, type}
}
)   

    return await apiCalls.handleNewResponse(
        await apiCalls.api.get(
            "temperature/",
            {
                ...apiCalls.get_auth_header(),
                params: {
                    portfolio, section, type
                }
            }
            // {
            //     ...apiCalls.get_auth_header(),
            //     ...params
            // }
        )
    );
}

async function getLastTemperature(portfolioName, section, type) {
    // console.log("portfolio name", portfolioName)

let params = {"options": "last", "section": section, "type": type, "portfolio": portfolioName};

    return await apiCalls.handleNewResponse(
        await apiCalls.api.get(
            "temperature/",
            {
                ...apiCalls.get_auth_header(),
                ...params
            }
        )
    );
}


export const apiTemperature = {
    addTemperature,
    getAllTemperature,
    getLastTemperature
    
    //
    //  deleteColour,
    // addColour,
    // getColourHistory
    // getAllColours,
    // getLastColour
}

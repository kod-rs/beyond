import { apiCalls } from './comm';


// async function deleteLocation(i) {

//     return await apiCalls.handleNewResponse(
//         await apiCalls.api.delete(
//             "locations/" + i,
//             JSON.stringify({
//             }),
//             apiCalls.get_auth_header()
//         )
//     );

// }

async function addColour(portfolio, colourHex) {
    /**
     * for user
     * for portfolio
     * add to history
     * 
     * colours
     *  portfolio [FK]
     *  colours_log
     *  
     * 
     */



    return await apiCalls.handleNewResponse(
        await apiCalls.api.post(
            "colour/",
            JSON.stringify({
                portfolio, colourHex
            }),
            apiCalls.get_auth_header()
        )
    );

}

// async function getLocationsFilterUsername(pn) {

//     return await apiCalls.handleNewResponse(
//         await apiCalls.api.get(
//             "locations/" + pn,
//             apiCalls.get_auth_header()
//         )
//     );

// }

async function getColourHistory(portfolioName) {
    console.log("portfolio name", portfolioName)
    return await apiCalls.handleNewResponse(
        await apiCalls.api.get(
            "colour/" + portfolioName,
            apiCalls.get_auth_header()
        )
    );
}

export const apiColour = {
    // deleteLocation,
    addColour,
    getColourHistory
    // getLocationsFilterUsername
}

import { apiCalls } from './comm';


async function deleteColour(i) {

    return await apiCalls.handleNewResponse(
        await apiCalls.api.delete(
            "colour/" + i,
            JSON.stringify({
            }),
            apiCalls.get_auth_header()
        )
    );

}

async function addColour(portfolio, colourHex) {
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
    deleteColour,
    addColour,
    getColourHistory
}

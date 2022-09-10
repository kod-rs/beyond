import { apiCalls } from './comm';

async function createOrUpdatePortfolio(currentName, newName, colour) {
    // todo csrf

    return await apiCalls.handleNewResponse(
        await apiCalls.api.post(
            "portfolio/",
            JSON.stringify({
                currentName,
                newName,
                colour
            }),
            apiCalls.get_auth_header()
        )
    );
}

async function deletePortfolio(currentName,) {
    // todo csrf

    return await apiCalls.handleNewResponse(
        await apiCalls.api.delete(
            "portfolio/" + currentName,
            apiCalls.get_auth_header()
        )
    );
}

async function getPortoflios() {

    return await apiCalls.handleNewResponse(
        await apiCalls.api.get(
            "portfolio/",
            apiCalls.get_auth_header()
        )
    );

}

async function patchPortoflios(portfolioOldName, portfolioNewName, portfolioNewColour) {
    console.log(portfolioOldName, portfolioNewName, portfolioNewColour)

    return await apiCalls.handleNewResponse(
        await apiCalls.api.patch(
            `portfolio/${portfolioOldName}`,
            // {
            //     'name': portfolioNewName,
            //     "colour": portfolioNewColour
            // },
            {
                ...apiCalls.get_auth_header(),

                'name': portfolioNewName,
                "colour": portfolioNewColour
            }
        )
    );

}


export const apiPortfolio = {
    createOrUpdatePortfolio,
    deletePortfolio,
    getPortoflios,
    patchPortoflios
}
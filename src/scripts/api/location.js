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

async function addLocation(portfolio, section, type, latitude, longitude, csrfToken) {

    return await apiCalls.handleNewResponse(
        await apiCalls.api.post(
            "locations/",
            JSON.stringify({
                portfolio,
                type, section, latitude, longitude, synchronizer_token: csrfToken
            }),
            apiCalls.get_auth_header()
        )
    );

}

async function getLocationsFilterUsername(pn) {

    return await apiCalls.handleNewResponse(
        await apiCalls.api.get(
            "locations/" + pn,
            apiCalls.get_auth_header()
        )
    );

}

export const apiLocation = {
    // deleteLocation,
    addLocation,
    getLocationsFilterUsername
}

const prod = false;

function getLocation () {

    if (!prod) {
        return "http://localhost:8000/"
    }

    return "https://www.camilibrary.fr/"
};
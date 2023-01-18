import axios from "axios";
// import https from "https";
import { getKeyValue, TOKEN_DICTIONARY } from "./storage.service.js";

const getWeather = async (city) => {
    const token = await getKeyValue(TOKEN_DICTIONARY.token);
    if (!token) {
        throw new Error(
            "Не задан ключ API. Задайте его через команду -t [API_KEY]"
        );
    }

    const { data } = await axios.get(
        "https://api.weatherapi.com/v1/current.json",
        {
            params: {
                key: token,
                q: city,
                lang: "ru",
            },
        }
    );
    
    return data;

    // const url = new URL("https://api.weatherapi.com/v1/current.json");
    // url.searchParams.append("q", city);
    // url.searchParams.append("key", token);
    // url.searchParams.append("lang", "ru");
    // // url.searchParams.append("units", "metrics");

    // https.get(url, (response) => {
    //     let res = "";
    //     response.on("data", (chunk) => {
    //         res += chunk;
    //     });

    //     response.on("end", () => {
    //         console.log(res);
    //     });
    // });
};

export { getWeather };

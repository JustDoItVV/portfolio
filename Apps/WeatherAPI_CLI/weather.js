#!/usr/bin/env node
import { getArgs } from "./helpers/args.js";
import { getWeather } from "./services/api.service.js";
import { printHelp, printSuccess, printError, printWeather } from "./services/log.service.js";
import { saveKeyValue, TOKEN_DICTIONARY, getKeyValue } from "./services/storage.service.js";

// Сохранить токен в json config в домашней директории
const saveToken = async (token) => {
    if (!token.length) {
        printError("Не передан токен");
        return;
    }
    try {
        await saveKeyValue(TOKEN_DICTIONARY.token, token);
        printSuccess("Токен сохранен");
    } catch (e) {
        printError(e.message);
    }
};

// Сохранить город в json config
const saveCity = async (city) => {
    if (!city.length) {
        printError("Не передан город");
        return;
    }
    try {
        await saveKeyValue(TOKEN_DICTIONARY.city, city);
        printSuccess("Город сохранен");
    } catch (e) {
        printError(e.message);
    }
};

// Обработка response ошибок API
const getForecast = async () => {
    try {
        const city = process.env.CITY ?? await getKeyValue(TOKEN_DICTIONARY.city)
        const weather = await getWeather(city);
        printWeather(weather);
    } catch (e) {
        if (e?.response?.status == 400) {
            printError("Неверно указан город");
        } else if (e?.response?.status == 401) {
            printError("Неверно указан токен");
        } else {
            printError(e.message);
        }
    }
};

// Инициализация CLI приложения
const initCLI = () => {
    const args = getArgs(process.argv);
    // console.log(process.env);
    if (args.h) {
        // Вывод help
        return printHelp();
    }
    if (args.s) {
        // Сохранить город
        return saveCity(args.s);
    }
    if (args.t) {
        // Сохранить токен
        return saveToken(args.t);
    }
    // Вывести погоду
    return getForecast();
};

initCLI();

// Бибилиотека для цветастого текста
import chalk from "chalk";
// Библиотека для убирания отступов тексат в коде при выоде в консоль
import dedent from "dedent-js";

const printError = (error) => {
    console.log(chalk.bgRed(" ERROR ") + " " + error);
};

const printSuccess = (message) => {
    console.log(chalk.bgGreen(" SUCCES ") + " " + message);
};

const printHelp = () => {
    console.log(
        dedent(
            `${chalk.bgCyan(" HELP ")}
            Без параметров - вывод погоды
            -s [CITY] для установки города
            -h для вывода помощи
            -t [API_KEY] для сохранения токена
            `
        )
    );
};

const printWeather = (res) => {
    console.log(
        dedent(
            `${chalk.bgYellow(" WEATHER ")} Погода в городе ${res.location.name}
            Местное время ${res.location.localtime}
            ${res.current.condition.text}
            Температура ${res.current.temp_c} °C
            Ощущается как ${res.current.feelslike_c} °C
            Ветер ${Number(res.current.wind_kph / 3.6).toFixed(1)} м/с, направление ${res.current.wind_dir}
            Влажность ${res.current.humidity}%

            `
        )
    );
};

export { printError, printSuccess, printHelp, printWeather };

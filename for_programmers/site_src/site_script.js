'use strict';


function test_working() {
    console.log("site_script.js загружен!");
}
test_working();


class ForProgrammer {
    /*
    Основной класс для сайта.
    */

    constructor() {
        console.log("ProgrammerGuide работает!");
        this.data = {}; // Объект для хранения загруженных данных
        this.loadAllData(); // Автоматически загружаем данные при создании экземпляра
    }

    async loadAllData() {
        try {
            // Получаем список всех JSON файлов в папке data
            const dataFiles = await this.getDataFileList();
            
            // Загружаем каждый файл
            for (const filename of dataFiles) {
                await this.loadJsonFile(filename);
            }
            
            console.log("Все данные загружены:", this.data);
            
        } catch (error) {
            console.error("Ошибка при загрузке данных:", error);
        }
    }

    async getDataFileList() {
        return ['data1.json', 'data2.json', 'data3.json']; // замените на реальные имена
    }

    async loadJsonFile(filename) {
        try {
            // Путь к файлу относительно текущего расположения скрипта
            const filePath = `../data/${filename}`;
            
            const response = await fetch(filePath);
            
            if (!response.ok) {
                throw new Error(`Ошибка загрузки ${filename}: ${response.status}`);
            }
            
            const jsonData = await response.json();
            
            // Сохраняем данные, используя имя файла как ключ (без расширения .json)
            const key = filename.replace('.json', '');
            this.data[key] = jsonData;
            
            console.log(`Файл ${filename} успешно загружен`);
            
        } catch (error) {
            console.error(`Ошибка при загрузке файла ${filename}:`, error);
        }
    }

    // Метод для получения загруженных данных
    getData(key = null) {
        if (key === null) {
            return this.data;
        }
        return this.data[key] || null;
    }

    // Метод для проверки, загружены ли данные
    isDataLoaded() {
        return Object.keys(this.data).length > 0;
    }
}

// Создаем глобальный экземпляр для использования на сайте
const forProgrammer = new ForProgrammer();

function main() {
    console.log("Вам не нужно запускать этот файл!")
}

import logging
# Импортируем модуль логирования для отслеживания событий и ошибок.
# Логирование полезно для отладки и мониторинга работы бота.
# Логи будут записываться с уровнем INFO и выше.

from telegram import Update
# Импортируем класс Update из библиотеки telegram.
# Он нужен для обработки входящих обновлений,
# таких как сообщения или команды от пользователей.

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)
# Импортируем необходимые классы из telegram.ext.
# ApplicationBuilder создает приложение бота,
# CommandHandler обрабатывает команды, MessageHandler — сообщения,
# filters фильтрует типы сообщений, ContextTypes — для асинхронности.

# Настраиваем базовое логирование для вывода информации
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
# Устанавливаем формат логов с временем, именем и уровнем.
# Уровень INFO позволяет видеть основные события.
# Логи будут полезны для проверки работы бота.

# Убираем лишние логи от httpx, чтобы терминал не захламлялся
logging.getLogger("httpx").setLevel(logging.WARNING)
# Устанавливаем уровень WARNING для httpx,
# чтобы не видеть все запросы GET и POST.
# Это делает вывод в терминале чище.
logger = logging.getLogger(__name__)
# Создаем логгер с именем текущего модуля для отладки.

# Задаем токен бота, полученный от BotFather
TOKEN = "your_bot_token_here"
# Токен — это ключ для связи бота с Telegram.
# Замените "your_bot_token_here" на токен, полученный от BotFather.
# Храните токен в безопасном месте, не публикуйте публично.

# Определяем функцию для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Функция отправляет приветственное сообщение при команде /start.
    # Асинхронная, так как использует await для отправки.
    await update.message.reply_text("Welcome to my echo bot!")
    # Отправляем пользователю текстовый ответ.

# Определяем функцию для эхо-ответов на сообщения
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Функция повторяет сообщение пользователя.
    # Используется для обработки текстовых сообщений.
    logger.info(f"Received message: {update.message.text}")
    # Логируем полученное сообщение для отладки.
    await update.message.reply_text(update.message.text)
    # Отправляем обратно тот же текст, что прислал пользователь.

# Создаем приложение бота с использованием токена
application = ApplicationBuilder().token(TOKEN).build()
# ApplicationBuilder создает экземпляр бота.
# Метод token() принимает токен для аутентификации.
# Метод build() завершает настройку приложения.

# Добавляем обработчик для команды /start
application.add_handler(CommandHandler("start", start))
# CommandHandler связывает команду /start с функцией start.
# Это позволяет боту реагировать на команду.

# Добавляем обработчик для текстовых сообщений
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
# MessageHandler обрабатывает текстовые сообщения.
# Фильтр TEXT & ~COMMAND исключает команды вроде /start.
# Это предотвращает эхо-ответ на команды.
# Связываем его с функцией echo.

# Запускаем бота в режиме опроса (polling)
application.run_polling()
# Метод run_polling() запускает бесконечный цикл.
# Бот будет получать обновления от Telegram.
# Остановить можно с помощью Ctrl+C в терминале.

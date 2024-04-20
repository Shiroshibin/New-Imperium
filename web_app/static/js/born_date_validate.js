const telegram_id = 77436892;


document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();

    const re = /^(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[0-2])\.([12]\d{3})$/;;
    const born_date_input = document.getElementById('born_date');

//    console.log([document.getElementById('born_date').value]);
//    console.log([re.test(born_date_input)]);

    // если введённыя дата соответствует регулярке
    if (re.test(born_date_input.value)) {
        // Устанавливаем значение скрытого поля
        document.getElementById('form_tg_id').value = telegram_id;

        // Отправляем форму
        this.submit();
    } else {
        born_date_input.style.border = "3px solid red"
    }
});

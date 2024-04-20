document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();

////    const re = /(([0-2]\d)|(3[01]))(0\d|1[0-2])([12]\d{3})/;
//    const re = new RegExp("/(([0-2]\d)|(3[01]))\.((0\d)|(1[0-2]))\.([12](\d{3}))/");
//    const born_date_input = document.getElementById('born_date');
//
//    console.log([document.getElementById('born_date').value]);
////    console.log([born_date_input.match(re)]);
//    console.log([re.test(born_date_input)]);

    // Отправляем форму
    this.submit();
});

const dateInput = document.getElementById("id_date")

const picker = MCDatepicker.create({
  el: "#id_date",
  dateFormat: "dd-mm-yyyy",
  closeOnBlur: true,
  selectedDate: new Date(),
})

dateInput.addEventListener("click", (evt) => {
  picker.open()
})
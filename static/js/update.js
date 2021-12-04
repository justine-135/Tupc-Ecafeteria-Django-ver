function itemFunc() {
  //DOM for item.html
  console.log("loadindex");
  console.log("LOADED: item.html");
  let foodName = document.querySelector('[name="item_name"]');
  let foodQuantity = document.querySelector("[name='item_quantity']");
  let foodPrice = document.querySelector("[name='item_price']");
  let imgUpload = document.querySelector("[name='item_img']");
  let drpDown = document.getElementById("dropdown");
  let tbodyBreakfast = document.getElementById("table-content-breakfast");
  let tbodyLunchmeal = document.getElementById("table-content-lunchmeal");
  let tbodyDrinks = document.getElementById("table-content-drinks");
  let tbodyAddons = document.getElementById("table-content-addons");
  let submitForm = document.getElementById("item-form");
  let modal = document.getElementById("modal-body");
  let addBtn = document.getElementById("add-button");
  let preview = document.getElementById("preview-insert-img");
  const clearForm = document.querySelector("#clear");
  const djangoForm = document.querySelector(".django-form");

  clearForm.addEventListener("click", () => {
    console.log("click");
    foodName.value = "";
    foodQuantity.value = "";
    foodPrice.value = "";
    imgUpload.value = "";
    preview.src = "";
  });

  drpDown.addEventListener("change", () => {
    const breakfastForm = document.querySelector(".bfast_form");
    const lunchmealForm = document.querySelector(".lmeal_form");
    const drinksForm = document.querySelector(".drinks_form");
    const addonsForm = document.querySelector(".addons_form");

    breakfastForm.style.display = "none";
    lunchmealForm.style.display = "none";
    drinksForm.style.display = "none";
    addonsForm.style.display = "none";
    console.log(drpDown.value);
    if (drpDown.value === "breakfast") {
      breakfastForm.style.display = "block";
      console.log("bselect");
    }
    if (drpDown.value === "lunchmeal") {
      lunchmealForm.style.display = "block";
    }
    if (drpDown.value === "beverage") {
      drinksForm.style.display = "block";
    }
    if (drpDown.value === "add-ons") {
      addonsForm.style.display = "block";
    }
  });

  // $("#id_item_name").keydown(function (e) {
  //   if (e.shiftKey || e.ctrlKey || e.altKey) {
  //     e.preventDefault();
  //   } else {
  //     var key = e.keyCode;
  //     //         keys a-z,0-9               numpad keys 0-9            minus sign    backspace
  //     if (
  //       (key >= 48 && key <= 90) ||
  //       (key >= 96 && key <= 105) ||
  //       key == 109 ||
  //       key == 8 ||
  //       key == 9 ||
  //       key == 32
  //     ) {
  //       console.log(foodName.value);
  //     } else {
  //       foodName.value = "food";
  //     }
  //   }
  // });

  foodQuantity.addEventListener("change", function (event) {
    // input must be an integer
    let inputQuantity = event.target;

    if (isNaN(parseInt(inputQuantity.value)) || inputQuantity.value <= 0) {
      inputQuantity.value = 1;
      console.log(
        "ERROR INPUT QUANTITY " + typeof parseInt(inputQuantity.value)
      );
    } else {
      foodQuantity.value = parseInt(inputQuantity.value);
    }
  });

  foodPrice.addEventListener("change", function (event) {
    // input must be integer or float
    let inputPrice = event.target;
    console.log(inputPrice);
    if (
      (isNaN(parseFloat(inputPrice.value)) &&
        isNaN(parseInt(inputPrice.value))) ||
      inputPrice.value <= 0
    ) {
      inputPrice.value = 1;
      console.log("ERROR INPUT PRICE" + +typeof parseFloat(inputPrice.value));
    } else if (inputPrice.value >= 1000) {
      inputPrice.value = 1000;
    }

    inputPrice = Math.round(inputPrice.value * 100) / 100; // round number to the nearest 2 dec.
    foodPrice.value = inputPrice;
  });

  let imgSrc = "";

  imgUpload.addEventListener("change", (event) => {
    console.log("change");
    if (event.target.files.length > 0) {
      imgSrc = URL.createObjectURL(event.target.files[0]);
      console.log(imgSrc);
      preview.src = imgSrc;
    }
  });

  submitForm.addEventListener("submit", function (e) {
    console.log("ey");
    if (
      isNaN(parseInt(foodQuantity.value)) ||
      isNaN(parseFloat(foodPrice.value)) ||
      imgSrc == "" ||
      foodName.value == ""
    ) {
      //if input not valid, prevent submit
      document.getElementById("confirmModalLabel").innerHTML =
        "Double check your inputs";
      console.log("ERROR: INPUT NOT VALID");
      e.preventDefault();
    }
  });

  addBtn.addEventListener("click", () => {
    document.getElementById("confirmModalLabel").innerHTML = "Confirmation";

    modal.innerHTML = `
      <img class="" id="modal-preview" alt='' src="${imgSrc}">
      Add this item to: <h6 class='popup'>${drpDown.value}</h6>  <hr>
      Item: <h6 class='popup'>${foodName.value}</h6> <hr>
      Quantity: <h6 class='popup'>${foodQuantity.value}</h6> <hr>
      Price: <h6 class='popup'>${foodPrice.value}</h6>
      `;
  });

  function getElementCount() {
    //show total item inside
    let breakfastCount = tbodyBreakfast.rows.length;
    let lunchmealCount = tbodyLunchmeal.rows.length;
    let drinksCount = tbodyDrinks.rows.length;
    let addonsCount = tbodyAddons.rows.length;

    document.getElementById("breakfast-count").textContent = breakfastCount;
    document.getElementById("lunchmeal-count").textContent = lunchmealCount;
    document.getElementById("drinks-count").textContent = drinksCount;
    document.getElementById("addons-count").textContent = addonsCount;
  }
  getElementCount();

  let btnDel = document.getElementsByClassName("rem");
  for (let i = 0; i < btnDel.length; i++) {
    btnDel[i].addEventListener("click", (e) => {
      let remove = confirm("Remove this item?");
      if (remove !== true) {
        e.preventDefault();
      }
    });
  }

  $(function () {
    // show tooltip
    $('[data-toggle="tooltip"]').tooltip({
      trigger: "hover",
    });
  });

  preview.src = djangoForm.childNodes[15].getAttribute("href");
  console.log(djangoForm.childNodes);
  djangoForm.childNodes[14].textContent = "";
  djangoForm.childNodes[15].innerHTML = "";
  djangoForm.childNodes[16].style.display = "none";
  djangoForm.childNodes[17].textContent = "";
}

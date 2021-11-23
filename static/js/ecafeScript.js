function indexFunc() {
  //DOM for index.html
  console.log("LOADED: index.html");

  let dateArray = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
  ]; // index of days

  let d = new Date();
  let n = dateArray[d.getDay()]; //display day name

  function formatAMPM(date) {
    //display minutes, seconds, AM and PM
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? "pm" : "am";
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = "00";
    let hourly = hours + 1;
    if (hours === 12) {
      hourly = 1;
    }
    var strTime =
      hours +
      ":" +
      minutes +
      " " +
      ampm +
      " - " +
      hourly +
      ":" +
      minutes +
      " " +
      ampm;
    return strTime;
  }

  console.log(formatAMPM(new Date()));
  document.getElementById("display-hour").value = formatAMPM(new Date()) + " ";

  let menuTitle = document.getElementById("menu-title");
  let selectBtn = document.getElementsByClassName("btn-select");
  const cover = document.getElementById("idCover");

  function clickCategories() {
    // show items when clicked
    for (let i = 0; i < selectBtn.length; i++) {
      selectBtn.item(i).onclick = function () {
        cover.style.zIndex = "1";
        if (this.id === "btn-breakfast") {
          menuTitle.textContent = "Breakfast";
        } else if (this.id === "btn-lunchmeals") {
          menuTitle.textContent = "Lunchmeals";
        } else if (this.id === "btn-beveragedrinks") {
          menuTitle.textContent = "Beverage/Drinks";
        } else if (this.id === "btn-addons") {
          menuTitle.textContent = "Add-ons";
        }
        function showBlur() {
          if (selectBtn[i].getAttribute("aria-expanded") == "true") {
            document.getElementById("select").innerHTML = `
            <pre>
   eat good 
  feel good
          </pre> 
            `;
            cover.style.zIndex = "6";
            menuTitle.textContent = "Home";
          }
        }
        document.getElementById("select").textContent = "";

        showBlur();
      };
    }
  }
  clickCategories();

  let itemImage = document.getElementById("idMenu").getElementsByTagName("img");
  let myPrice = document.getElementById("myPrice");
  myPrice.style.fontWeight = "bolder";

  function clickImage() {
    // do something when item is clicked
    for (let i = 0; i < itemImage.length; i++) {
      itemImage[i].addEventListener("click", itemClicked);
    }
  }
  clickImage();

  function itemClicked(event) {
    let thisItem = event.target;
    let getName = thisItem.getAttribute("name");
    let getPrice = thisItem.getAttribute("value2");
    let getQuantity = thisItem.getAttribute("value");
    addToCart(getName, getPrice, getQuantity);
    deleteRow();
  }

  function countQuantity() {
    let quantityElement = document.getElementsByClassName("quantity-element");
    for (let i = 0; i < quantityElement.length; i++) {
      let inputVal = quantityElement[i];
      inputVal.addEventListener("change", (event) => {
        let quantityInput = event.target;
        if (
          isNaN(parseInt(quantityInput.value)) ||
          parseInt(quantityInput.value) <= 0
        ) {
          quantityInput.value = 1;
        } else if (
          parseInt(quantityInput.value) >
          parseInt(quantityInput.getAttribute("max"))
        ) {
          quantityInput.value = quantityInput.getAttribute("max");
        }
        totalPrice();
      });
    }
  }

  function totalPrice() {
    // total price amount
    let idPrice = 0;
    let inside = document.getElementsByClassName("content-inside");
    for (let i = 0; i < inside.length; i++) {
      let quantity = inside[i].getElementsByClassName("quantity-element")[0];
      let price = inside[i].getElementsByClassName("pricing")[0];
      idPrice = idPrice + parseFloat(price.value) * parseFloat(quantity.value);
    }
    idPrice = Math.round(idPrice * 100) / 100;
    myPrice.setAttribute("value", idPrice);
    submitForm1();
    deleteRow();
  }

  function addToCart(itemName, itemPrice, itemQuantity) {
    // add item to orders
    let eachItemName = document.getElementsByClassName("name-par");
    let createDiv = document.createElement("div");

    for (let i = 0; i < eachItemName.length; i++) {
      if (eachItemName[i].value == itemName) {
        alert("Item already added!");
        return;
      }
    }

    let formContents = `
    <div class="row content-inside" id="${itemName}">
      <input type="textbox" class="name-par pl-1 col-5 col-xl-4" value='${itemName}' name="foods" readonly>
      <input type="textbox" class="pricing col-3 col-xl-3" value="${itemPrice}" name="prices" readonly>
      <input class="quantity-element col-2 col-xl-3" type="number" min="1" max="${itemQuantity}" value="1" name="quantity">
      <button class="del col-2 col-xl-1 material-icons" id="id-delete" type="button">clear</button>
    </div>
    `;
    createDiv.innerHTML = formContents;

    let itemRow = document.getElementById("inside");
    itemRow.appendChild(createDiv);

    countQuantity();
    totalPrice();
    getTotal();
  }

  function deleteRow() {
    //delete individual orders
    let del = document.getElementsByClassName("del");
    for (let i = 0; i < del.length; i++) {
      del[i].addEventListener("click", function (event) {
        event.target.parentNode.parentNode.remove();
        totalPrice();
        getTotal();
      });
    }
  }

  function writeCaption() {
    //write caption for each image
    let caption = document.getElementsByClassName("caption");
    for (let i = 0; i < caption.length; i++) {
      let getImg = caption.item(i).parentNode.firstElementChild;
      let getImgQuantity = getImg.getAttribute("value");
      let getImgName = getImg.getAttribute("name");
      let getImgPrice = getImg.getAttribute("value2");

      caption.item(i).getElementsByTagName("h5")[0].textContent = getImgName;
      caption.item(i).getElementsByTagName("h6")[0].textContent =
        "Quantity: " + getImgQuantity;
      caption.item(i).getElementsByTagName("h6")[1].textContent =
        "Price: P" + getImgPrice;
    }
  }
  writeCaption();

  function getTotal() {
    // total items selected
    let totalCount = document.getElementsByClassName("content-inside").length;
    let orderCount = document.getElementById("order-count");
    orderCount.textContent = totalCount;
  }

  function clearRow() {
    // clear all items
    let container = document.getElementsByClassName("content")[0];
    let resetBtn = document.getElementById("idReset");
    resetBtn.addEventListener("click", function () {
      while (container.firstChild) {
        container.removeChild(container.firstChild);
        totalPrice();
        getTotal();
      }
    });
  }
  clearRow();

  let indexForm = document.getElementById("index-form");

  function submitForm1() {
    indexForm.addEventListener("submit", (e) => {
      // purchase items

      if (myPrice.value == 0 || isNaN(parseFloat(myPrice.value))) {
        e.preventDefault();
        return;
      }
    });
  }
  submitForm1();

  $(function () {
    // show tooltip
    $('[data-toggle="tooltip"]').tooltip({
      trigger: "hover",
    });
  });
}

function itemFunc() {
  //DOM for item.html
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
  const clearForm = document.querySelector('#clear');

  clearForm.addEventListener('click', ()=>{
    console.log('click')
    foodName.value = '';
    foodQuantity.value = '';
    foodPrice.value = '';
    imgUpload.value = '';
    preview.src = '';
  })

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
    let breakfastTbl = document.getElementById("id-table-item-breakfast")
      .childNodes[3];
    let lunchmealTbl = document.getElementById("id-table-item-lunchmeal")
      .childNodes[3];
    let drinksTbl = document.getElementById("id-table-item-drinks")
      .childNodes[3];
    let addonTbl = document.getElementById("id-table-item-addons")
      .childNodes[3];

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
    } else {
      //input is valid, submit

      if (drpDown.value === "breakfast") {
        // if duplicates, prevent submit

        for (let i = 0; i < breakfastTbl.rows.length; i++) {
          //check dupplicates
          if (breakfastTbl.rows[i].childNodes[1].innerHTML == foodName.value) {
            document.getElementById("confirmModalLabel").innerHTML =
              "This item is already added";

            e.preventDefault();
          }
        }
      }
      if (drpDown.value === "lunchmeal") {
        for (let i = 0; i < lunchmealTbl.rows.length; i++) {
          //check dupplicates
          if (lunchmealTbl.rows[i].childNodes[1].innerHTML == foodName.value) {
            document.getElementById("confirmModalLabel").innerHTML =
              "This item is already added";

            e.preventDefault();
          }
        }
      }
      if (drpDown.value === "beverage") {
        for (let i = 0; i < drinksTbl.rows.length; i++) {
          //check dupplicates
          if (drinksTbl.rows[i].childNodes[1].innerHTML == foodName.value) {
            document.getElementById("confirmModalLabel").innerHTML =
              "This item is already added";

            e.preventDefault();
          }
        }
      }
      if (drpDown.value === "add-ons") {
        for (let i = 0; i < addonTbl.rows.length; i++) {
          //check dupplicates
          if (addonTbl.rows[i].childNodes[1].innerHTML == foodName.value) {
            document.getElementById("confirmModalLabel").innerHTML =
              "This item is already added";

            e.preventDefault();
          }
        }
      }
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
}

function inventoryFunc() {
  //DOM for item.html

  console.log("LOADED: inventory.html");
  let indexSales = 0;
  let successSales = 0;
  let cancelSales = 0;
  let checkBtn = document.getElementsByClassName("change");
  let banBtn = document.getElementsByClassName("change2");
  let salesValue = document.getElementById("id-sales-value");
  let successValue = document.getElementById("id-success-value");
  let cancelValue = document.getElementById("id-cancel-value");
  let table = document.getElementById("tbl-inventory");
  let clearTable = document.getElementById("reset-btn");
  let inventory = document.getElementById("inventory-body");

  inventory.addEventListener("mouseover", () => {
    // update time on mouse hover
    document.getElementById("id-time").textContent =
      formatAMPM(new Date()) + " ";
    document.getElementById("id-time").appendChild(createI);
  });

  for (let i = 1; i < table.rows.length; i++) {
    //loop table rows
    let tablerows2 = table.rows[i];
    let tableCellPrice = tablerows2.cells.item(3).textContent;
    tablerows2.style.backgroundColor = "white";
    updateSales(tablerows2, tableCellPrice);
  }

  function updateSales(tablerows2, tableCellPrice) {
    // change text color, update no. of sales, success, and cancel
    if (tablerows2.childNodes[9].textContent === "SUCCESS") {
      tablerows2.childNodes[9].style.color = "#1261A0";
      indexSales = indexSales + parseInt(tableCellPrice);
      salesValue.textContent = "P " + indexSales;
      successSales++;
      successValue.textContent = successSales;
    } else if (tablerows2.childNodes[9].textContent === "CANCELLED") {
      tablerows2.childNodes[9].style.color = "#e12120";
      cancelSales++;
      cancelValue.textContent = cancelSales;
    }
  }

  for (let i = 0; i < banBtn.length; i++) {
    banBtn[i].addEventListener("click", (e) => {
      if (
        banBtn[i].parentNode.parentNode.childNodes[9].textContent == "SUCCESS"
      ) {
        let yesNo = confirm(
          'Mark this order as "CANCELLED"? This cannot be reverted.'
        );
        if (yesNo !== true) {
          e.preventDefault();
        }
      } else {
        e.preventDefault();
      }
    });
  }

  let dateArray = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
  ]; // index of days

  let d = new Date();
  let n = dateArray[d.getDay()]; //display day name

  document.getElementById("date-name").textContent = n + " ";

  function formatAMPM(date) {
    //display minutes, seconds, AM and PM
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? "pm" : "am";
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? "0" + minutes : minutes;
    var strTime = hours + ":" + minutes + " " + ampm;
    return strTime;
  }

  let createI = document.createElement("i");
  createI.setAttribute("class", "far fa-clock inventory-icons");

  console.log(formatAMPM(new Date()));
  document.getElementById("id-time").textContent = formatAMPM(new Date()) + " ";
  document.getElementById("id-time").appendChild(createI);

  clearTable.addEventListener("click", (e) => {
    // append new table if true
    let choose = confirm("Erase all data from the table?");
    if (choose !== true) {
      e.preventDefault();
    }
  });

  $(function () {
    $('[data-toggle="tooltip"]').tooltip({
      trigger: "hover",
    });
  });
}

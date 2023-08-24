const statusbar = document.getElementById("statusbar");
const timeDate = document.createElement("DIV");
statusbar.appendChild(timeDate);

const order = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    "timestamp": new Date()
};

let config = {}

setInterval(() => {
    const dat = new Date();
    const d = dat.toLocaleDateString('de-CH');
    const t = dat.toLocaleTimeString('de-CH');
    timeDate.innerText = `${d} ${t}`;
}, 1000);


const counter = document.getElementsByClassName("counter");
const minusButton = document.getElementsByClassName("minus");
const plusButton = document.getElementsByClassName("plus");


for (let m of minusButton) {
    const but = m.firstElementChild;
    but.addEventListener("click", () => {
        minusCounter(but.dataset.typeid);
    });
}


for (let p of plusButton) {
    const but = p.firstElementChild;
    but.addEventListener("click", () => {
        plusCounter(but.dataset.typeid);
    });
}

const minusCounter = (c) => {
    if (order[c] !== 0) order[c] = order[c] - 1;
    updatePiadinaCounter(c);
};
const plusCounter = (c) => {
    order[c] = order[c] + 1;
    updatePiadinaCounter(c);
};

const updatePiadinaCounter = (c) => {
    const coun = counter[c];
    const h = coun.firstElementChild;
    h.innerText = order[c];
    updateLabels();
    checkPlaceOrderButton();
};

let to = undefined;

const placeOrderCustomer = () => {
    if (order["0"] === 0 && order["1"] === 0 && order["2"] === 0 && order["3"] === 0) return;
    order.timestamp = new Date();
    pywebview.api.placeOrder(JSON.stringify(order));
    to = setTimeout(() => {
        resetOrder();
        clearTimeout(to);
    }, config.system.timeout);
};


const resetOrder = () => {
    order["0"] = 0;
    order["1"] = 0;
    order["2"] = 0;
    order["3"] = 0;
    updateLabels();
    checkPlaceOrderButton();
};

const updateLabels = () => {
    let o = 0;
    for (let c of counter) {
        const lbl = c.firstElementChild;
        lbl.innerText = order[o];
        o++;
    }
};

const checkPlaceOrderButton = () => {
    const placeOrderCustomerButton = document.getElementById("place-order-customer-button");
    if (order["0"] === 0 && order["1"] === 0 && order["2"] === 0 && order["3"] === 0) {
        placeOrderCustomerButton.disabled = true;
        return;
    }
    placeOrderCustomerButton.disabled = false;
};

function updateUI(response) {
    console.log("Loaded Config " + JSON.stringify(response));
    config = response;

    const p0 = document.getElementById("piadina-0");
    const p1 = document.getElementById("piadina-1");
    const p2 = document.getElementById("piadina-2");
    const p3 = document.getElementById("piadina-3");

    const piadinaImg = document.getElementsByClassName("piadina-img");

    p0.innerText = response[0].name;
    p1.innerText = response[1].name;
    p2.innerText = response[2].name;
    p3.innerText = response[3].name;

    let o = 0;
    for (let i of piadinaImg) {
        i.src = "./static/" + response[o].image;
        o++;
    }

    updateLabels();
    checkPlaceOrderButton();
}

window.addEventListener('pywebviewready', function () {
    pywebview.api.getConfig().then(updateUI);
});
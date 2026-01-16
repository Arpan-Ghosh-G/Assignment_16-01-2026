// async function sendMessage() {
//     const input = document.getElementById("message");
//     const message = input.value;

//     if (!message) return;

//     const chatBox = document.getElementById("chat-box");
//     chatBox.innerHTML += `<p><b>You:</b> ${message}</p>`;

//     const response = await fetch("/chat", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json"
//         },
//         body: JSON.stringify({ message })
//     });

//     const data = await response.json();
//     chatBox.innerHTML += `<p><b>Ronaldo:</b> ${data.reply}</p>`;

//     input.value = "";
// }







// JS for form


async function generateForm() {
    const prompt = document.getElementById("prompt").value;

    const response = await fetch("/generate-form", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt })
    });

    const schema = await response.json();
    renderForm(schema);
}

function renderForm(schema) {
    const container = document.getElementById("form-container");
    container.innerHTML = "";

    const form = document.createElement("form");
    form.innerHTML = `<h4>${schema.title}</h4>`;

    schema.fields.forEach(field => {
        const div = document.createElement("div");
        div.className = "mb-3";

        let inputField = "";

        if (field.type === "textarea") {
            inputField = `<textarea class="form-control" name="${field.name}" ${field.required ? "required" : ""}></textarea>`;
        } else {
            inputField = `<input type="${field.type}" class="form-control" name="${field.name}" ${field.required ? "required" : ""}>`;
        }

        div.innerHTML = `
            <label class="form-label">${field.label}</label>
            ${inputField}
        `;

        form.appendChild(div);
    });

    const submitBtn = document.createElement("button");
    submitBtn.type = "submit";
    submitBtn.className = "btn btn-success";
    submitBtn.innerText = "Submit";

    form.appendChild(submitBtn);

    form.onsubmit = submitForm;

    container.appendChild(form);
}

async function submitForm(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const data = {};

    formData.forEach((value, key) => {
        data[key] = value;
    });

    const response = await fetch("/submit-form", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    document.getElementById("result").innerText = JSON.stringify(result, null, 2);

}

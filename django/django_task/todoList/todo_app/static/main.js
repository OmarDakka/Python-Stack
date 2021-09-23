let createCategory = async(e) => {
    e.preventDefault();

    let title = document.getElementById('title');
    let user_id = document.getElementById('created_by').value;
    let id = document.getElementById('id');

    if (id.value == 0) {
        await axios.post('/todo/category', {
            title: title.value,
            user_id
        });
    } else {
        await axios.put(`/todo/category/${id.value}`, {
            title: title.value,
            user_id
        });
    }

    await getCategories();

    var myModal = document.getElementById('exampleModal');
    var modal = bootstrap.Modal.getInstance(myModal) // Returns a Bootstrap modal instance
    modal.hide();

    title.value = "";
    id.value = 0;
}

let deleteCategory = async(id) => {
    await axios.delete(`/todo/category/${id}`);
    await getCategories();
}

let getCategories = async() => {
    let result = (await axios.get('/todo/category')).data.items;

    let div = document.getElementById('categories');

    while (div.firstChild) {
        div.removeChild(div.firstChild);
    }

    result.forEach(category => {
        let category_div = document.createElement('div');
        category_div.classList.add("card");
        category_div.style.width = "18rem";

        let category_body = document.createElement('div');
        category_body.classList.add("card-body");

        let category_title = document.createElement('h5');
        category_title.classList.add("card-title");
        category_title.innerText = category.title;

        let category_delete = document.createElement("button");
        category_delete.classList.add("btn");
        category_delete.classList.add("btn-danger");
        category_delete.innerText = "Delete";
        category_delete.onclick = () => deleteCategory(category.id);

        let category_edit = document.createElement("button");
        category_edit.classList.add("btn");
        category_edit.classList.add("btn-primary");
        category_edit.innerText = "Edit";

        category_edit.onclick = () => {
            let title = document.getElementById('title');
            title.value = category.title;
            let id = document.getElementById('id');
            id.value = category.id;

            var myModal = document.getElementById('exampleModal');
            var modal = bootstrap.Modal.getOrCreateInstance(myModal) // Returns a Bootstrap modal instance
            modal.show();
        };

        category_body.appendChild(category_title);
        category_body.appendChild(category_edit);
        category_body.appendChild(category_delete);
        category_div.appendChild(category_body);

        div.appendChild(category_div);
    });
}

let categoryForm = document.getElementById('categoryForm');

categoryForm.onsubmit = createCategory;

getCategories();
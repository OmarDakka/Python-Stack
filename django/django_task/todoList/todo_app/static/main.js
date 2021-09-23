let createCard = (width = "18rem") => {
    let div = document.createElement('div');
    div.classList.add("card");
    div.style.width = width;

    let body = document.createElement('div');
    body.classList.add("card-body");

    let title = document.createElement('h5');
    title.classList.add("card-title");

    return { div, body, title };
};

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
        let category_div = createCard();

        category_div.title.innerText = category.title;

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

        let create_task = document.createElement("button");
        create_task.classList.add("btn");
        create_task.classList.add("btn-primary");
        create_task.innerText = "Create Task";
        create_task.onclick = () => {
            let id = document.getElementById('category_id');
            id.value = category.id;

            var myModal = document.getElementById('taskModal');
            var modal = bootstrap.Modal.getOrCreateInstance(myModal) // Returns a Bootstrap modal instance
            modal.show();
        };

        category_div.body.appendChild(category_div.title);

        category.tasks.forEach(task => {
            let taskCard = createCard();

            taskCard.title.innerText = task.title;

            let desc = document.createElement("p");
            desc.innerText = task.description;

            let dueDate = document.createElement("p");
            dueDate.innerText = task.duedate;

            let task_delete = document.createElement("button");
            task_delete.classList.add("btn");
            task_delete.classList.add("btn-danger");
            task_delete.innerText = "Delete";
            task_delete.onclick = () => deleteTask(task.id);
            
            let task_edit = document.createElement("button");
            task_edit.classList.add("btn");
            task_edit.classList.add("btn-primary");
            task_edit.innerText = "Edit Task";
            task_edit.onclick = () => {
                let title = document.getElementById('taskTitle');
                title.value = task.title;
                let description = document.getElementById('description');
                description.value = task.description;
                let duedate = document.getElementById('duedate');
                duedate.value = task.duedate;
                let id = document.getElementById('task_id');
                id.value = task.id;
                let category_id = document.getElementById('category_id');
                category_id.value = category.id;
    
                var myModal = document.getElementById('taskModal');
                var modal = bootstrap.Modal.getOrCreateInstance(myModal) // Returns a Bootstrap modal instance
                modal.show();
            };

            taskCard.body.appendChild(taskCard.title);
            taskCard.body.appendChild(desc) 
            taskCard.body.appendChild(dueDate);
            taskCard.body.appendChild(task_edit); 
            taskCard.body.appendChild(task_delete); 
            taskCard.div.appendChild(taskCard.body);
            category_div.body.appendChild(taskCard.div);
        });

        category_div.body.appendChild(create_task);
        category_div.body.appendChild(category_edit);
        category_div.body.appendChild(category_delete);
        category_div.div.appendChild(category_div.body);

        div.appendChild(category_div.div);
    });
}

let createTask = async(e) => {
    e.preventDefault();

    let taskTitle = document.getElementById("taskTitle");
    let user_id = document.getElementById("task_created_by").value;
    let id = document.getElementById("task_id");
    let description = document.getElementById("description");
    let duedate = document.getElementById("duedate");
    let category_id = document.getElementById("category_id");

    if (id.value == 0) {
        await axios.post('/todo/task', {
            title: taskTitle.value,
            user_id,
            description: description.value,
            duedate: duedate.value,
            category_id: category_id.value
        });
    } else {
        await axios.put(`/todo/task/${id.value}`, {
            title: taskTitle.value,
            user_id,
            description: description.value,
            duedate: duedate.value,
            category_id: category_id.value
        });
    }

    await getCategories();

    var myModal = document.getElementById('taskModal');
    var modal = bootstrap.Modal.getInstance(myModal) // Returns a Bootstrap modal instance
    modal.hide();

    taskTitle.value = "";
    description.value = "";
    duedate.value = "";
    category_id.value = 0;
    id.value = 0;

}

let deleteTask = async(id) => {
    await axios.delete(`/todo/task/${id}`);
    await getCategories();
}

let categoryForm = document.getElementById('categoryForm');

categoryForm.onsubmit = createCategory;

let taskForm = document.getElementById('taskForm');

taskForm.onsubmit = createTask;

getCategories();
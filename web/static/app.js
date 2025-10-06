document.getElementById('formVenta').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const response = await fetch('/agregar_venta', {
        method: 'POST',
        body: formData
    });
    const data = await response.json();
    alert(data.mensaje);
});

document.getElementById('btnVerVentas').addEventListener('click', async () => {
    const response = await fetch('/ver_ventas');
    const data = await response.json();

    const tbody = document.querySelector('#tablaVentas tbody');
    tbody.innerHTML = '';
    data.forEach(row => {
        const tr = document.createElement('tr');
        tr.innerHTML = `<td>${row.categoria}</td><td>${row.total_ventas}</td>`;
        tbody.appendChild(tr);
    });
});

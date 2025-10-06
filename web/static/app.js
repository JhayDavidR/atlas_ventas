const API_URL = "http://127.0.0.1:5001";

document.addEventListener("DOMContentLoaded", () => {
  cargarClientes();
  cargarProductos();
  cargarVentas();
});

document.getElementById("formVenta").addEventListener("submit", async (e) => {
  e.preventDefault();

  const cliente_id = document.getElementById("cliente_id").value;
  const id_producto = document.getElementById("id_producto").value;
  const cantidad = document.getElementById("cantidad").value;
  const fecha_venta = new Date().toISOString().slice(0, 19).replace("T", " ");

  try {
    const response = await fetch(`${API_URL}/agregar_venta`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ cliente_id, id_producto, cantidad, fecha_venta }),
    });

    const data = await response.json();
    Swal.fire({
      icon: data.status === "success" ? "success" : "error",
      title: data.message,
      timer: 2000,
      showConfirmButton: false,
    });

    if (data.status === "success") cargarVentas();
  } catch (error) {
    Swal.fire("Error", error.message, "error");
  }
});

document.getElementById("btnETL").addEventListener("click", async () => {
  const confirm = await Swal.fire({
    title: "¿Ejecutar ETL?",
    text: "Esto actualizará los datos en la base destino",
    icon: "question",
    showCancelButton: true,
    confirmButtonText: "Sí, ejecutar",
    cancelButtonText: "Cancelar",
  });

  if (confirm.isConfirmed) {
    const response = await fetch(`${API_URL}/ejecutar_etl`, { method: "POST" });
    const data = await response.json();
    Swal.fire({
      icon: data.status === "success" ? "success" : "error",
      title: data.message,
      timer: 2500,
      showConfirmButton: false,
    });
    if (data.status === "success") cargarVentas();
  }
});

async function cargarClientes() {
  const response = await fetch(`${API_URL}/clientes`);
  const data = await response.json();
  const select = document.getElementById("cliente_id");
  select.innerHTML = '<option value="">Seleccione...</option>';
  data.forEach(c => {
    select.innerHTML += `<option value="${c.id_cliente}">${c.nombre}</option>`;
  });
}

async function cargarProductos() {
  const response = await fetch(`${API_URL}/productos`);
  const data = await response.json();
  const select = document.getElementById("id_producto");
  select.innerHTML = '<option value="">Seleccione...</option>';
  data.forEach(p => {
    select.innerHTML += `<option value="${p.id_producto}">${p.nombre_producto}</option>`;
  });
}

async function cargarVentas() {
  const response = await fetch(`${API_URL}/ventas_por_categoria`);
  const data = await response.json();
  const tbody = document.querySelector("#tablaVentas tbody");
  tbody.innerHTML = "";

  if (data.status === "success") {
    data.data.forEach((v) => {
      const row = `
        <tr>
          <td>${v.categoria}</td>
          <td>${v.total_ventas}</td>
          <td>${v.total_unidades}</td>
        </tr>`;
      tbody.innerHTML += row;
    });
  }
}

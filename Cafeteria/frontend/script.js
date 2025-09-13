const API_BASE = 'http://localhost:8000';
let carrito = [];
let productosCache = [];

// Cargar productos al iniciar
document.addEventListener('DOMContentLoaded', () => {
    cargarProductos();
    cargarProductosCache();
});

async function cargarProductosCache() {
    try {
        const response = await fetch(`${API_BASE}/productos/`);
        productosCache = await response.json();
    } catch (error) {
        console.error('Error al cargar cache de productos:', error);
    }
}

async function cargarProductos() {
    try {
        const response = await fetch(`${API_BASE}/productos/`);
        const productos = await response.json();
        mostrarProductos(productos);
    } catch (error) {
        console.error('Error al cargar productos:', error);
    }
}

async function cargarProductosPorCategoria(categoria) {
    try {
        const response = await fetch(`${API_BASE}/productos/categoria/${categoria}`);
        const productos = await response.json();
        mostrarProductos(productos);
    } catch (error) {
        console.error('Error al cargar productos:', error);
    }
}

function mostrarProductos(productos) {
    const contenedor = document.getElementById('productos');
    contenedor.innerHTML = '';

    productos.forEach(producto => {
        if (producto.disponible) {
            const productoCard = document.createElement('div');
            productoCard.className = 'producto-card';
            productoCard.innerHTML = `
                <img src="${producto.imagen || 'https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=400&h=300&fit=crop'}" 
                     alt="${producto.nombre}" onerror="this.src='https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=400&h=300&fit=crop'">
                <h3>${producto.nombre}</h3>
                <p>${producto.descripcion}</p>
                <div class="precio">$${producto.precio.toFixed(2)}</div>
                <button class="agregar-carrito" onclick="agregarAlCarrito(${producto.id})">
                    Agregar al carrito
                </button>
            `;
            contenedor.appendChild(productoCard);
        }
    });
}

function agregarAlCarrito(productoId) {
    carrito.push(productoId);
    actualizarCarrito();
    mostrarNotificacion('Producto agregado al carrito!');
}

function actualizarCarrito() {
    const itemsCarrito = document.getElementById('itemsCarrito');
    const totalElement = document.getElementById('total');
    
    itemsCarrito.innerHTML = '';
    let total = 0;

    const conteo = {};
    carrito.forEach(id => {
        conteo[id] = (conteo[id] || 0) + 1;
    });

    Object.keys(conteo).forEach(id => {
        const producto = productosCache.find(p => p.id === parseInt(id));
        if (producto) {
            const subtotal = producto.precio * conteo[id];
            total += subtotal;

            const li = document.createElement('li');
            li.innerHTML = `
                <span>${producto.nombre} x${conteo[id]}</span>
                <span>$${subtotal.toFixed(2)}</span>
                <button onclick="removerDelCarrito(${id})">❌</button>
            `;
            itemsCarrito.appendChild(li);
        }
    });

    totalElement.textContent = total.toFixed(2);
}

function removerDelCarrito(productoId) {
    const index = carrito.indexOf(parseInt(productoId));
    if (index > -1) {
        carrito.splice(index, 1);
        actualizarCarrito();
    }
}

function mostrarNotificacion(mensaje) {
    const notificacion = document.createElement('div');
    notificacion.className = 'notificacion';
    notificacion.textContent = mensaje;
    notificacion.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: #4CAF50;
        color: white;
        padding: 15px;
        border-radius: 5px;
        z-index: 1000;
    `;
    
    document.body.appendChild(notificacion);
    
    setTimeout(() => {
        notificacion.remove();
    }, 3000);
}

// Manejar envío del formulario de pedido
document.getElementById('pedidoForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const nombre = document.getElementById('nombre').value;
    const email = document.getElementById('email').value;
    
    if (carrito.length === 0) {
        alert('El carrito está vacío');
        return;
    }
    
    if (!nombre || !email) {
        alert('Por favor completa todos los campos');
        return;
    }
    
    try {
        const response = await fetch(`${API_BASE}/pedidos/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                cliente_nombre: nombre,
                cliente_email: email,
                productos: carrito,
                total: 0 // Se calculará automáticamente en el backend
            })
        });
        
        if (response.ok) {
            const pedido = await response.json();
            alert(`¡Pedido realizado con éxito! Número de pedido: ${pedido.id}`);
            carrito = [];
            actualizarCarrito();
            document.getElementById('pedidoForm').reset();
        } else {
            alert('Error al realizar el pedido');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error al conectar con el servidor');
    }
});
---
title: Number Detection
shortDescription: Aplicación web que reconoce números dibujados usando un modelo TensorFlow.js directamente en el navegador.
link: https://github.com/pausegarra/number-detection
featured: true
links:
  - title: GitHub
    url: https://github.com/pausegarra/number_detection
    className: "bg-gradient-to-r from-purple-500 to-pink-600"
  - title: Website
    url: https://number-detection.pausegarra.es
    className: "bg-gradient-to-r from-green-500 to-purple-500"
tech:
  - JS
  - HTML
  - CSS
  - JavaScript
  - TensorFlow.js
  - Python
  - Tensorflow
features:
  - Reconocimiento de números en tiempo real con TensorFlow.js
  - Funciona completamente en el navegador sin backend
---

![Number Detection](/number-detection.png)

Este proyecto es una aplicación web interactiva basada en navegador que permite dibujar dígitos numéricos y recibir resultados de reconocimiento instantáneos usando un modelo de deep learning impulsado por TensorFlow.js. Es un ejemplo de cómo las tecnologías web modernas y el machine learning pueden combinarse para crear aplicaciones inteligentes y autónomas que se ejecutan por completo en el cliente, sin infraestructura de backend.

La funcionalidad central se basa en una red neuronal convolucional (CNN) entrenada para reconocer dígitos del conocido dataset MNIST. Este conjunto de datos contiene decenas de miles de números escritos a mano, recopilados y etiquetados para entrenar modelos de machine learning. El entrenamiento original probablemente se realizó en Python con TensorFlow, y después el modelo se convirtió a un formato compatible con TensorFlow.js para hacer inferencias directamente en el navegador.

Cuando los usuarios acceden a la aplicación, encuentran una interfaz minimalista e intuitiva donde pueden dibujar libremente un dígito sobre un canvas usando el ratón o la pantalla táctil. En cuanto el dibujo está listo, la aplicación captura la imagen, la procesa redimensionando, normalizando y centrando la entrada para ajustarla al formato esperado por el modelo (normalmente 28x28 píxeles en escala de grises) y la envía a la red neuronal para generar una predicción.

Una de las principales ventajas de esta aplicación es que todos los cálculos se realizan localmente en el navegador. Esto garantiza privacidad total (no se envían datos a ningún servidor), latencia muy baja (los resultados son casi instantáneos) y soporte completo sin conexión. Además, demuestra las capacidades crecientes de WebAssembly y de librerías de ML basadas en JavaScript como TensorFlow.js, haciendo la IA avanzada accesible sin depender de servicios cloud ni instalaciones pesadas en el cliente.

Desde el punto de vista técnico, el proyecto está construido con HTML, CSS y JavaScript, junto con TensorFlow.js para la inferencia del modelo. La lógica de entrenamiento y los scripts de conversión probablemente se implementaron en Python dentro del ecosistema original de TensorFlow. Esta combinación de tecnologías ilustra un flujo completo de machine learning, desde la preparación y el entrenamiento en Python hasta la inferencia en tiempo real en el navegador con JavaScript.

Este proyecto sirve como demostración práctica de:
* Desplegar modelos de IA en entornos web usando TensorFlow.js.
* Realizar reconocimiento de dígitos en tiempo real del lado del cliente.
* Construir aplicaciones de machine learning centradas en la privacidad y sin backend.
* Conectar los ecosistemas Python y JavaScript con una arquitectura limpia y modular.

Tanto si eres una persona entusiasta del machine learning, un desarrollador frontend explorando IA o un profesor que quiere mostrar ML en acción, este proyecto ofrece un ejemplo claro, interactivo y técnicamente sólido de inteligencia en el navegador.

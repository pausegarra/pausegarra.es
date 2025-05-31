---
title: Number Detection
shortDescription: A web app that recognizes drawn numbers using a TensorFlow.js model directly in the browser.
link: https://github.com/pausegarra/number-detection
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
  - Real-time number recognition using a TensorFlow.js model
  - Runs entirely in the browser with no backend required
---

![Number Detection](/number-detection.png)

This project is an interactive, browser-based web application that allows users to draw numerical digits and receive instant recognition results using a deep learning model powered by TensorFlow.js. It exemplifies how modern web technologies and machine learning can work together to create intelligent, self-contained applications that run entirely on the client side without any backend infrastructure.

The core functionality is built around a convolutional neural network (CNN) that has been trained to recognize digits from the widely known MNIST dataset. This dataset consists of tens of thousands of handwritten digits collected and labeled for training machine learning models. The original training was likely performed in Python using TensorFlow, after which the model was converted into a format compatible with TensorFlow.js for inference directly in the browser.

When users access the application, they are presented with a minimal and intuitive interface where they can freely draw a digit on a canvas using their mouse or touchscreen. As soon as the digit is drawn, the application captures the image, processes it by resizing, normalizing, and centering the input to match the expected input format of the model (usually 28x28 grayscale pixels), and then feeds it into the neural network to generate a prediction.

One of the key benefits of this application is that all computations are performed locally in the browser. This ensures complete privacy (no data is sent to a server), extremely low latency (results are near-instantaneous), and full offline support. This approach also demonstrates the growing capabilities of WebAssembly and JavaScript-based ML libraries like TensorFlow.js, making advanced AI accessible without requiring cloud services or heavy client-side installations.

From a technical perspective, the project is built using HTML, CSS, and JavaScript, alongside TensorFlow.js for model inference. The training logic and conversion scripts were likely implemented in Python using the original TensorFlow ecosystem. This combination of technologies illustrates a full-stack machine learning workflow—from data preparation and training in Python to real-time inference in the browser with JavaScript.

This project serves as a practical demonstration of:
* Deploying AI models in web environments using TensorFlow.js.
* Performing real-time, client-side digit recognition.
* Building privacy-first machine learning applications without backends.
* Bridging the Python and JavaScript ecosystems in a clean, modular architecture.

Whether you’re a machine learning enthusiast, a frontend developer exploring AI, or a teacher looking to show ML in action, this project provides a clear, interactive, and technically sound example of browser-based intelligence in action.
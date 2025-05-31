---
title: SendIf
shortDescription: A web application that allows users to calculate the difficulty of a given mountain route.
link: https://github.com/pausegarra/sendif
links:
  - title: GitHub
    url: https://github.com/pausegarra/sendif
    className: "bg-gradient-to-r from-purple-500 to-pink-600"
  - title: Website
    url: https://sendif.pausegarra.es
    className: "bg-gradient-to-r from-green-500 to-purple-500"
tech:
  - NodeJS
  - NextJS
  - Docker
features:
  - Server-side rendering
  - Server Actions
---

![SendIf](/sendif.png)

SendIf is a full-stack web application designed to assist climbers, hikers, and outdoor enthusiasts in evaluating the difficulty of mountain routes before setting out on their adventures. The application provides a modern, responsive interface that allows users to input route characteristics and receive a computed difficulty rating based on multiple technical and environmental parameters. This makes SendIf an essential tool for planning, safety assessment, and training progression in both recreational and professional mountain activities.

The platform operates with a focus on usability, performance, and precision. Built with Next.js and Node.js, it benefits from the modern web stack’s capabilities, including server-side rendering (SSR) for improved SEO and load performance, and the latest React Server Actions to manage data seamlessly between client and server.

Users can define custom mountain routes by specifying variables such as elevation gain and total length. The application applies a set of internal algorithms to assess and output a consistent difficulty grade—similar in spirit to the French Alpine Grade or the UIAA scale—providing a reliable and transparent estimation of challenge level.

The application is containerized using Docker, which simplifies deployment across various environments, from local development to scalable production infrastructure. This architecture ensures high portability and maintainability, whether the service is self-hosted or deployed in the cloud.

SendIf is open source and available on GitHub, allowing the climbing and development community to contribute to its algorithms, design, or localization. The project is designed with extensibility in mind, enabling future integration with GPS tracking tools, route databases, or collaborative planning features.

Key aspects of the project include:
* Dynamic route evaluation with a detailed difficulty scoring algorithm.
* Responsive UI suitable for desktop and mobile use in field conditions.
* Server-side rendering for better performance and SEO.
* Secure and scalable architecture built on modern technologies like Docker and Node.js.
* Open contribution model through GitHub to encourage community feedback and improvements.

Whether you’re planning a solo scramble, coordinating a group climb, or logging completed ascents, SendIf helps bring objectivity and structure to the art of route assessment. It empowers users to make informed decisions in the mountains—where preparation often makes the difference between success and risk.
export const locales = [
  {
    code: "en",
    label: "English",
    nativeLabel: "English",
    htmlLang: "en",
    ogLocale: "en_US",
  },
  {
    code: "es",
    label: "Spanish",
    nativeLabel: "Español",
    htmlLang: "es",
    ogLocale: "es_ES",
  },
] as const;

export type Locale = (typeof locales)[number]["code"];

export const defaultLocale: Locale = "en";
export const fallbackLocale: Locale = "en";
export const localeStorageKey = "pausegarra:locale";
export const siteUrl = "https://pausegarra.com";

export const siteCopy = {
  en: {
    seo: {
      homeTitle: "Pau Segarra | Backend Software Engineer Portfolio",
      homeDescription:
        "Portfolio of Pau Segarra, a backend software engineer specializing in scalable microservices, APIs, and cloud infrastructure.",
      homeKeywords:
        "backend engineer portfolio, software engineer, microservices, APIs, cloud infrastructure, Pau Segarra",
      projectsTitle: "Projects | Backend Engineering Portfolio of Pau Segarra",
      projectsDescription:
        "Explore backend engineering projects by Pau Segarra, including scalable APIs, cloud-native architectures, event-driven systems, and real-world implementations using Java, Quarkus, OpenFGA, and more.",
      projectsKeywords:
        "backend projects, API architecture, cloud-native projects, event-driven systems, software engineering portfolio",
      projectKeywordsBase:
        "backend project, software architecture, Pau Segarra",
    },
    navigation: {
      home: "Home",
      projects: "Projects",
      contact: "Contact",
      languageLabel: "Language",
    },
    hero: {
      title: "Pau Segarra",
      subtitle: "Turning complexity into elegant software solutions",
      description:
        "I'm a Software Engineer focused on crafting robust server architectures, RESTful APIs, and optimized database systems that power scalable and modern web applications.",
      primaryCta: "View My Work",
      secondaryCta: "Get In Touch",
    },
    about: {
      title: "About Me",
      paragraphs: [
        "I'm a Software Engineer with over 5 years of experience in backend development, specialized in building scalable and high-performance server-side applications. I design and implement robust RESTful APIs, optimize relational and NoSQL databases, and architect distributed systems using modern DevOps practices.",
        "My core technologies include Java, Spring Boot, Quarkus, Node.js, NestJS, React, Docker, Kubernetes, and PostgreSQL. I follow clean code principles, domain-driven design, and I'm passionate about solving complex technical challenges with simple and elegant solutions.",
      ],
      stats: [
        { value: "50+", label: "Projects Completed" },
        { value: "5+", label: "Years Experience" },
      ],
    },
    skills: {
      title: "Tech Stack",
      description:
        "A compact snapshot of the tools I reach for most across backend, infrastructure, and product work.",
    },
    projects: {
      title: "Featured Projects",
      pageTitle: "Projects",
      pageDescription:
        "A collection of backend engineering projects, APIs, cloud-native systems, and practical product work.",
      button: "View All Projects",
      keyFeatures: "Key Features:",
    },
    projectDetail: {
      visitPrefix: "Visit",
      technologies: "Technologies",
      features: "Features",
      breadcrumbs: {
        home: "Home",
        projects: "Projects",
      },
    },
    contact: {
      title: "Let's Work Together",
      description:
        "Ready to build something amazing? I'm always open to discussing new opportunities and interesting projects.",
      cards: {
        email: "Email",
        linkedin: "LinkedIn",
        github: "GitHub",
      },
    },
    footer: {
      developedBy: "Designed & developed by",
      rights: "All rights reserved.",
    },
  },
  es: {
    seo: {
      homeTitle: "Pau Segarra | Portfolio de Backend Software Engineer",
      homeDescription:
        "Portfolio de Pau Segarra, backend software engineer especializado en microservicios escalables, APIs e infraestructura cloud.",
      homeKeywords:
        "portfolio backend engineer, software engineer, microservicios, APIs, infraestructura cloud, Pau Segarra",
      projectsTitle: "Proyectos | Portfolio de Ingeniería Backend de Pau Segarra",
      projectsDescription:
        "Explora proyectos de ingeniería backend de Pau Segarra, incluyendo APIs escalables, arquitecturas cloud-native, sistemas event-driven e implementaciones reales con Java, Quarkus, OpenFGA y más.",
      projectsKeywords:
        "proyectos backend, arquitectura de APIs, proyectos cloud-native, sistemas event-driven, portfolio ingeniería software",
      projectKeywordsBase:
        "proyecto backend, arquitectura software, Pau Segarra",
    },
    navigation: {
      home: "Inicio",
      projects: "Proyectos",
      contact: "Contacto",
      languageLabel: "Idioma",
    },
    hero: {
      title: "Pau Segarra",
      subtitle: "Convirtiendo complejidad en soluciones de software elegantes",
      description:
        "Soy Software Engineer centrado en crear arquitecturas de servidor robustas, APIs REST y sistemas de bases de datos optimizados que impulsan aplicaciones web escalables y modernas.",
      primaryCta: "Ver mi trabajo",
      secondaryCta: "Contactar",
    },
    about: {
      title: "Sobre mí",
      paragraphs: [
        "Soy Software Engineer con más de 5 años de experiencia en desarrollo backend, especializado en construir aplicaciones server-side escalables y de alto rendimiento. Diseño e implemento APIs REST robustas, optimizo bases de datos relacionales y NoSQL, y arquitecto sistemas distribuidos usando prácticas modernas de DevOps.",
        "Mis tecnologías principales incluyen Java, Spring Boot, Quarkus, Node.js, NestJS, React, Docker, Kubernetes y PostgreSQL. Sigo principios de clean code, domain-driven design y me apasiona resolver desafíos técnicos complejos con soluciones simples y elegantes.",
      ],
      stats: [
        { value: "50+", label: "Proyectos completados" },
        { value: "5+", label: "Años de experiencia" },
      ],
    },
    skills: {
      title: "Stack técnico",
      description:
        "Una vista compacta de las herramientas que más uso en backend, infraestructura y producto.",
    },
    projects: {
      title: "Proyectos destacados",
      pageTitle: "Proyectos",
      pageDescription:
        "Una colección de proyectos de ingeniería backend, APIs, sistemas cloud-native y trabajo práctico de producto.",
      button: "Ver todos los proyectos",
      keyFeatures: "Funciones clave:",
    },
    projectDetail: {
      visitPrefix: "Visitar",
      technologies: "Tecnologías",
      features: "Funciones",
      breadcrumbs: {
        home: "Inicio",
        projects: "Proyectos",
      },
    },
    contact: {
      title: "Trabajemos juntos",
      description:
        "¿Quieres construir algo increíble? Siempre estoy abierto a hablar de nuevas oportunidades y proyectos interesantes.",
      cards: {
        email: "Correo",
        linkedin: "LinkedIn",
        github: "GitHub",
      },
    },
    footer: {
      developedBy: "Diseñado y desarrollado por",
      rights: "Todos los derechos reservados.",
    },
  },
} as const;

export type SiteCopy = (typeof siteCopy)[Locale];

export function isLocale(value: string): value is Locale {
  return locales.some((locale) => locale.code === value);
}

export function getLocaleMeta(locale: Locale) {
  return locales.find((item) => item.code === locale) ?? locales[0];
}

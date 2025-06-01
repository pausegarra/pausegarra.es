import { defineCollection, z } from "astro:content";

const projects = defineCollection({
  schema: z.object({
    title: z.string(),
    shortDescription: z.string(),
    tech: z.array(z.string()),
    features: z.array(z.string()),
    link: z.string().nullable(),
    featured: z.boolean(),
    links: z.array(z.object({
      title: z.string(),
      url: z.string(),
      className: z.string()
    }))
  })
});

export const collections = {
  projects
};
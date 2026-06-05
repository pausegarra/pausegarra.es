import { getCollection, type CollectionEntry } from "astro:content";
import { type Locale, isLocale } from "./i18n";

export type ProjectEntry = CollectionEntry<"projects">;

export function getProjectLocale(slug: string): Locale | null {
  const [firstSegment] = slug.split("/");
  return firstSegment && isLocale(firstSegment) ? firstSegment : null;
}

export function getProjectSlug(slug: string): string {
  const [, ...rest] = slug.split("/");
  return rest.join("/");
}

export async function getProjectsForLocale(locale: Locale) {
  const projects = await getCollection("projects");
  return projects.filter((project) => getProjectLocale(project.slug) === locale);
}

export async function getFeaturedProjectsForLocale(locale: Locale) {
  const projects = await getProjectsForLocale(locale);
  return projects.filter((project) => project.data.featured);
}

export async function getProjectForLocale(locale: Locale, id: string) {
  const projects = await getCollection("projects");
  return projects.find((project) => project.slug === `${locale}/${id}`) ?? null;
}

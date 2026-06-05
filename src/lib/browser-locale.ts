import { fallbackLocale, isLocale, localeStorageKey, locales, type Locale } from "./i18n";

const localeCodes = locales.map((locale) => locale.code);

export function getStoredLocale(): Locale | null {
  if (typeof localStorage === "undefined") {
    return null;
  }

  try {
    const storedLocale = localStorage.getItem(localeStorageKey);
    return storedLocale && isLocale(storedLocale) ? storedLocale : null;
  } catch {
    return null;
  }
}

export function getBrowserPreferredLocale(): Locale {
  const candidates = [...navigator.languages, navigator.language]
    .filter(Boolean)
    .map((value) => value.toLowerCase());

  for (const candidate of candidates) {
    const exactMatch = localeCodes.find((locale) => locale === candidate);
    if (exactMatch) {
      return exactMatch;
    }

    const prefix = candidate.split("-")[0];
    const prefixMatch = localeCodes.find((locale) => locale === prefix);
    if (prefixMatch) {
      return prefixMatch;
    }
  }

  return fallbackLocale;
}

export function getPathWithoutLocale(pathname: string): string {
  const parts = pathname.split("/").filter(Boolean);
  if (parts.length > 0 && isLocale(parts[0])) {
    parts.shift();
  }

  return `/${parts.join("/")}/`.replace(/\/+/g, "/") || "/";
}

export function getLocalizedPath(locale: Locale, pathname: string): string {
  const pathWithoutLocale = getPathWithoutLocale(pathname);
  return pathWithoutLocale === "/" ? `/${locale}/` : `/${locale}${pathWithoutLocale}`;
}

export function getPreferredLocalePath(pathname: string): string {
  const storedLocale = getStoredLocale();
  const preferredLocale = storedLocale ?? getBrowserPreferredLocale();
  return getLocalizedPath(preferredLocale, pathname);
}

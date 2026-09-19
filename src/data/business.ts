/**
 * Canonical business identity. Every legal page, the footer and the JSON-LD
 * schema read from here so the published details can never drift apart —
 * Safepay verification compares these across the site.
 */

export const business = {
  legalName: 'Muhammad Omar Farooq',
  tradingAs: 'DiviDesignPro',
  displayName: 'DiviDesignPro',
  siteUrl: 'https://www.dividesignpro.com',
  email: 'contact@dividesignpro.com',

  /** Boilerplate used by the Organization and LocalBusiness schema builders. */
  description:
    'Freelance Divi and WordPress developer building fast, SEO-optimised websites for small businesses worldwide. 10+ years of experience, 100+ sites delivered.',

  /** Public asset paths. The schema builders resolve these against siteUrl, the
   *  same way SEOMeta resolves ogImage. */
  logo: '/logo.png',
  ogImage: '/og-images/home-og.png',

  phoneLocal: { display: '+92 310 1418307', href: '+923101418307' },
  phoneInternational: { display: '+1 (307) 445-3714', href: '+13074453714' },

  address: {
    line1: '213-A, Street #01',
    line2: 'Mohallah Salamatpura, Darogawala',
    city: 'Lahore',
    postalCode: '54000',
    region: 'Punjab',
    country: 'Pakistan',
  },

  /** This is a service-area business (see google-business-profile.md), not a
   *  storefront — so areaServed carries the local signal rather than geo
   *  coordinates, which we deliberately do not invent. */
  areaServed: ['Lahore', 'Pakistan', 'Worldwide'],

  /** Spans the maintenance entry tier ($99/mo) up to a full custom build. */
  priceRange: '$99 - $2500',

  /** Support hours in PKT (UTC+5), taken from google-business-profile.md. */
  openingHours: [
    { days: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], opens: '09:00', closes: '18:00' },
    { days: ['Saturday'], opens: '10:00', closes: '16:00' },
  ],

  sameAs: [
    'https://www.linkedin.com/in/muhammad-omar-farooq-wp/',
    'https://www.facebook.com/divithemesolution',
  ],

  currency: 'USD',
  effectiveDate: '14 September 2026',
  lastUpdated: '14 September 2026',

  refundTurnaround: '7 to 14 business days',
  complaintAcknowledgement: '5 business days',
  complaintResolution: '30 days',
} as const;

/** Address as an array of display lines, omitting any blank field. */
export function addressLines(): string[] {
  const { line1, line2, city, postalCode, region, country } = business.address;
  const cityLine = [city, postalCode].filter(Boolean).join(' ');
  return [line1, line2, `${cityLine}, ${region}`, country].filter(Boolean);
}

/** Single-line address, e.g. for schema.org PostalAddress or a meta tag. */
export function addressOneLine(): string {
  return addressLines().join(', ');
}

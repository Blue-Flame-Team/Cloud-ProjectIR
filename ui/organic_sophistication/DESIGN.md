---
name: Organic Sophistication
colors:
  surface: '#fbf9f5'
  surface-dim: '#dbdad6'
  surface-bright: '#fbf9f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3ef'
  surface-container: '#efeeea'
  surface-container-high: '#eae8e4'
  surface-container-highest: '#e4e2de'
  on-surface: '#1b1c1a'
  on-surface-variant: '#504442'
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f0ed'
  outline: '#827471'
  outline-variant: '#d4c3bf'
  surface-tint: '#755750'
  primary: '#361f1a'
  on-primary: '#ffffff'
  primary-container: '#4e342e'
  on-primary-container: '#c19c94'
  inverse-primary: '#e5beb5'
  secondary: '#984629'
  on-secondary: '#ffffff'
  secondary-container: '#ff9875'
  on-secondary-container: '#782e13'
  tertiary: '#735c00'
  on-tertiary: '#ffffff'
  tertiary-container: '#cca830'
  on-tertiary-container: '#4f3e00'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad2'
  primary-fixed-dim: '#e5beb5'
  on-primary-fixed: '#2b1611'
  on-primary-fixed-variant: '#5c403a'
  secondary-fixed: '#ffdbcf'
  secondary-fixed-dim: '#ffb59c'
  on-secondary-fixed: '#390c00'
  on-secondary-fixed-variant: '#793014'
  tertiary-fixed: '#ffe088'
  tertiary-fixed-dim: '#e9c349'
  on-tertiary-fixed: '#241a00'
  on-tertiary-fixed-variant: '#574500'
  background: '#fbf9f5'
  on-background: '#1b1c1a'
  surface-variant: '#e4e2de'
typography:
  h1:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Public Sans
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-sm:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
  max-width: 1280px
---

## Brand & Style

The design system is centered on a philosophy of "Tactile Serenity." It moves away from the cold, clinical nature of traditional tech interfaces toward a world that feels organic, artisanal, and deeply trustworthy. The aesthetic bridges the gap between high-end editorial print and modern digital interfaces.

The style is a refined evolution of **Neumorphism**, stripped of its usability pitfalls. It utilizes soft, directional light sources to create gentle extrusions and recesses, making the UI feel like it has been physically molded from soft clay or premium paper. The atmosphere is consistently warm, evoking the feeling of a sunlit studio or a quiet library. 

**Core Principles:**
- **Organic Depth:** Depth is created through light and shadow, never through harsh lines.
- **Approachable Luxury:** Use of rich, earthy tones to convey high value without being exclusionary.
- **Breatheability:** Generous white space (or "cream space") ensures that the content remains the primary focus.

## Colors

The palette for the design system is rooted in earth and light. It avoids pure blacks and stark whites in favor of complex, warm neutrals.

- **Primary (Rich Brown):** Used for primary actions, high-level headings, and structural elements. It provides the grounding force for the interface.
- **Secondary (Terracotta):** A vibrant but earthy accent used for interactive highlights, notifications, or call-to-action buttons that need to stand out from the brown.
- **Tertiary (Muted Gold):** Reserved for prestige elements, premium features, or subtle decorative accents.
- **Neutrals (Cream & Beige):** These form the foundation. The "Base" cream is for the overall page background, while the "Surface" beige is used for elevated cards and containers to create a soft, layered effect.

## Typography

The design system utilizes **Public Sans** across all levels to maintain a clean, institutional clarity that feels both modern and timeless. 

The typographic hierarchy is built on high contrast between size and weight to ensure legibility. Large headings use a tighter letter spacing and a heavier weight to feel authoritative and grounded. Body text is set with generous line-height to maximize readability against the soft-colored backgrounds. Labels are consistently uppercase with slightly increased tracking to provide a distinct visual rhythm for metadata and UI controls.

## Layout & Spacing

The design system employs a **fixed-fluid hybrid grid**. Content is contained within a maximum width for desktop to ensure line lengths remain comfortable, while margins and gutters adapt fluidly on smaller viewports.

Spacing follows an 8px rhythm, emphasizing "breathing room." Large components and sections should be separated by 'LG' or 'XL' spacing to maintain the sophisticated, uncluttered feel. Internal padding within cards and containers should be generous—never cramped—to reinforce the soft, inviting nature of the UI.

## Elevation & Depth

Depth in this design system is achieved through **Soft UI Light Physics**. Rather than floating objects with high-contrast drop shadows, elements appear to be part of the surface itself.

- **Soft Extrusion:** Buttons and primary cards use two shadows. A light-colored shadow (Cream/White) on the top-left and a warm, tinted dark shadow (Soft Brown/Tan) on the bottom-right. This creates the "molded" effect.
- **Subtle Inset:** Input fields and search bars use an inner shadow to appear recessed into the surface, suggesting a functional area that can be filled.
- **Tonal Tiers:** Secondary depth is achieved by placing 'Surface' beige elements on 'Base' cream backgrounds. Low-opacity brown outlines (5-10% opacity) may be used for additional definition on high-density screens.

## Shapes

The shape language is fundamentally **rounded and organic**. Sharp corners are avoided to maintain the "trustworthy and inviting" brand promise.

- **Standard Elements:** Buttons, inputs, and small widgets use a 0.5rem (8px) radius.
- **Containers:** Large cards and informational blocks use a 1rem (16px) radius to emphasize their structural importance.
- **Featured Elements:** Hero sections or large imagery may use 1.5rem (24px) for a softer, more custom aesthetic.

## Components

### Buttons
Primary buttons are styled with the rich brown background and white or cream text. They feature a subtle "Soft UI" lift. Secondary buttons use the terracotta accent to highlight specific alternative actions.

### Cards
Cards are the primary organizational unit. They should have a background color of the 'Surface' beige. Use the dual-shadow technique sparingly—only on the main container to avoid visual clutter.

### Input Fields
Inputs are slightly recessed (inner shadow) with a soft beige background. The focus state should be indicated by a thin, warm terracotta border or a subtle glow, rather than a harsh color change.

### Chips & Tags
Chips are pill-shaped and use low-contrast tonal fills (e.g., a slightly darker tan than the background) with rich brown text. They should feel lightweight and secondary to the main content.

### Selection Controls
Checkboxes and radio buttons use the rich brown for their active states. The "checkmark" or "dot" should be in the cream background color to ensure high contrast and a clean look.

### Navigation
The navigation should feel airy. Use ample horizontal spacing between links. Active states should be indicated by a subtle terracotta underline or a soft, recessed background shape.
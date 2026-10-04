# Section choices shown before each component draft

If sections have not already been selected, show this list with a short, plain-language description for each item. If the user already selected sections in the request or saved work, reuse that set and skip the selection question. Let the user select any relevant subset. Mark a section `not applicable` when the component cannot support it, and explain briefly. The names are labels for selection, not a mandatory document outline.

Use the project's primary language for each description; keep the stable English section name after a Persian label when the conversation is in Persian. Prefer a real multi-select control with individually clickable, accessible checkboxes and a clear confirm action when the conversation supports one. The confirm action must return the selected section names to the assistant. If no such control is available, show separate plain Markdown bullets and ask the user to reply with section names. Do not render `- [ ]` or other fake checkbox marks in that fallback. Do not ask users to decipher numbers. Do not put all ten items into one form field, option label, or continuous paragraph: some question interfaces flatten line breaks and make mixed RTL/LTR text unreadable. Keep evidence caveats in a short sentence after the choices, not inside their labels.

For a Persian conversation, use this presentation pattern, adapting the descriptions to the component:

- معرفی (`Overview`) — کاربرد کامپوننت و زمان استفاده از آن.
- اجزا (`Anatomy`) — بخش‌های اصلی و اختیاری.
- انواع و سایزها (`Variants and sizes`) — گزینه‌های موجود و کاربرد هرکدام.
- حالت‌ها (`States`) — حالت‌های بصری و تعاملی.
- رفتار (`Behavior`) — اکشن‌ها و نتیجهٔ آن‌ها.
- راهنمای استفاده (`Usage rules`) — بایدها و نبایدهای تأییدشده.
- محتوا (`Content`) — متن، طول، شکست خط و کوتاه‌شدن.
- ریسپانسیو و راست‌به‌چپ (`Responsive and RTL`) — رفتار در عرض‌ها و جهت‌های مختلف.
- دسترس‌پذیری (`Accessibility`) — فوکوس، کیبورد و اعلام‌ها.
- پیاده‌سازی (`Implementation`) — تنظیمات و محدودیت‌های توسعه.

- **Overview** — what the component does and when to choose it.
- **Anatomy** — named parts and optional slots.
- **Variants and sizes** — supported forms and when each applies.
- **States** — supported visual or interactive states.
- **Behavior** — confirmed actions and their results.
- **Usage rules** — do and do not guidance backed by local decisions.
- **Content** — wording, lengths, wrapping, truncation, and empty content.
- **Responsive and RTL** — behavior across widths and text directions when supported.
- **Accessibility** — confirmed semantics, focus, keyboard, contrast, and announcements.
- **Implementation** — authored properties, configuration values, and developer constraints.

Before writing, briefly echo the selected sections as plain bullets. The user's explicit selection already confirms the set; do not ask for an additional approval just to proceed. Do not invent a rule simply to fill a selected section; ask a focused question or flag the gap. Do not silently add unselected sections to the final document.

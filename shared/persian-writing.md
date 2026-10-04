# Persian component documentation

Read this guide before writing or revising Persian documentation, captions, annotations, or Markdown alt text.

- Use natural, concise, semi-formal Persian with Persian ی/ک, appropriate half-spaces, and Persian punctuation. Prefer familiar product terms to literal translation or invented equivalents.
- Do not attach Persian ezafe marks to English identifiers. Write «در حالت `Compact`» rather than modifying the identifier. Avoid filler such as «لازم به ذکر است» and abstract technical phrasing when a plain explanation is clearer.
- Use familiar product terms such as «اکشن»، «استایل»، «سایز» and «ریسپانسیو» when they fit the audience. Use «انواع» as the heading for variant or type choices. For text beside a control, use «عنوان» in prose; an authored property named `Label` remains `Label`.
- Use a common Persian transliteration for a component name in prose. Preferred spellings: Badge → بج, Tab → تب, Tag → تگ, List Item → لیست‌آیتم, Switch → سوییچ, Tooltip → تولتیپ. A project's configured terminology may override these examples.
- In the main Persian heading, include the English component name in parentheses, such as «آواتار (Avatar)».
- Preserve user-visible property, variant, state, size, and configuration identifiers exactly as authored, including spelling, spaces, and capitalization. For example, write «سوییچ» in prose while keeping `Type=Switch` unchanged. Under visual specimens, keep exact source variant and state values.
- Use a Persian semantic part name as the primary Anatomy label. An exact property identifier can appear as secondary text. Do not use a raw API binding suffix such as `#123:45` in public text unless explicitly requested.
- For measurements in visuals, use English digits, one space, and `px`, such as `8 px`.
- Keep each caption to one confirmed, useful point. Do not mention an image that has not been delivered.
- Consult external design-system pages for research, but keep the published component document focused on the user's confirmed local rules. Avoid naming research references in publication prose unless the user explicitly wants a comparison.
- Use consistent terms and section structures within a component. Prefer complete sentences, short paragraphs, and real bullets for parallel items.

- Keep opacity distinct from transparency. For full opacity, use «کدری کامل» or an explicit `opacity=1`; do not call it «شفافیت کامل». Lower opacity means the element is more transparent, not less transparent. Preserve authored numeric values.

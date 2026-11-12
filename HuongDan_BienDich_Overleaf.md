# Hướng dẫn biên dịch LaTeX cho người mới (Overleaf + Local)

> Áp dụng cho đồ án GIT - GitHub - GitLab, môn ASPX (.NET Framework 4.8.1), nhóm 3 thành viên.
> Source cần biên dịch: `BaoCao_LaTeX/main.tex`, `BaoCao_LaTeX/tailieu_thamkhao.bib`, `Slide_LaTeX/slide.tex`, hình trong `HinhAnh/*.svg`.
> Compiler chuẩn của nhóm: **pdfLaTeX**. Báo cáo dùng `article` + `fontenc` T5 + `babel` vietnamese. Slide dùng `beamer`.

## 0. Tổng quan 2 cách biên dịch

| Cách | Khi nào dùng | Cần cài gì | Ưu điểm |
|---|---|---|---|
| A. Overleaf (online) | Người mới, máy yếu, cần làm nhóm | Chỉ cần trình duyệt + mạng | Không cài đặt, tự có gói tiếng Việt, dễ share link |
| B. Local (offline) | Máy cá nhân, cần biên dịch nhanh, nộp bản cuối | TeX Live hoặc MiKTeX + TeXstudio/VS Code | Biên dịch nhanh, chủ động gói, dễ debug lỗi nặng |

**Quy tắc chung:** báo cáo biên dịch 4 lượt (`pdflatex` -> `bibtex` -> `pdflatex` -> `pdflatex`), slide biên dịch 2 lượt (`pdflatex` 2 lần). Luôn giữ file `.tex` ở encoding UTF-8.

---

## Phần A. Biên dịch trên Overleaf (8 bước, cho người mới)

### Bước 1. Tạo tài khoản và project trắng cho báo cáo
1. Vào trang Overleaf, đăng nhập (nên dùng email sinh viên để dễ share nhóm).
2. Bấm **New Project** -> **Blank Project**, đặt tên `BaoCao_ASPX_Nhom3TV`.
3. Xóa nội dung mẫu trong `main.tex` để chuẩn bị upload source của nhóm.

### Bước 2. Upload toàn bộ thư mục BaoCao_LaTeX
1. Trong project vừa tạo, bấm nút **Upload** (mũi tên lên) -> **Select from your computer**.
2. Chọn tất cả file trong thư mục `BaoCao_LaTeX/`: `main.tex`, `tailieu_thamkhao.bib`, các file `chuong*.tex` nếu có.
3. Nếu Overleaf hỏi ghi đè `main.tex` thì chọn **Overwrite**.
4. Kiểm tra cây thư mục bên trái: `main.tex` nằm ở gốc project, file `.bib` nằm cùng cấp với `main.tex`.

### Bước 3. Chọn đúng compiler pdfLaTeX
1. Bấm nút **Menu** (góc trái trên) để mở **Project Settings**.
2. Mục **Compiler** chọn `pdfLaTeX` (bắt buộc, vì source dùng `fontenc` T5).
3. Mục **Main document** chọn `main.tex`.
4. Mục **Spellcheck language** có thể để English, không ảnh hưởng tiếng Việt.

### Bước 4. Bấm Recompile lần đầu và đọc log
1. Bấm nút xanh **Recompile** (hoặc Ctrl+Enter).
2. Đợi 10-30 giây. Nếu PDF hiện bên phải là thành công bước đầu.
3. Nếu thanh trạng thái báo đỏ, bấm **View Log** (biểu tượng bên cạnh Recompile) để xem lỗi, đối chiếu Phần C bên dưới.

### Bước 5. Biên dịch đủ 4 lượt để hiện mục lục và tài liệu tham khảo
1. Overleaf bình thường tự chạy đủ lượt khi bấm **Recompile** 2-3 lần liên tiếp.
2. Cách chắc chắn: bấm **Recompile** -> đợi xong -> bấm tiếp **Recompile** lần 2 và lần 3.
3. Kiểm tra: mục lục có số trang, cuối báo cáo có danh mục tài liệu tham khảo, không còn dòng `?` thay cho số chương.
4. Nếu vẫn hiện `[?]` thì bấm **Clear Cached Files** trong Menu rồi Recompile lại.

### Bước 6. Sửa lỗi, cảnh báo và kiểm tra tiếng Việt
1. Tìm các cảnh báo `Overfull \hbox`, `Citation ... undefined`, `There were undefined references` trong log.
2. Sửa theo bảng 10 lỗi ở Phần C, mỗi lần sửa 1 chỗ rồi Recompile để biết lỗi nào đã hết.
3. Kiểm tra tiếng Việt: chữ `đ`, `ê`, `ộ`, `ữ` hiện đúng, không mất dấu, không thành ô vuông.
4. Kiểm tra hình TikZ: các hình vẽ bằng TikZ phải hiện ngay, chưa cần upload SVG.

### Bước 7. Tải PDF báo cáo về máy
1. Bấm nút **Download PDF** (mũi tên xuống, cạnh Recompile) để tải `main.pdf`.
2. Đổi tên thành `BaoCao_ASPX_Nhom3TV.pdf` để nộp, không để tên `main.pdf` dễ nhầm với slide.
3. Mở PDF kiểm tra: bìa có tên + MSSV 3 thành viên, mục lục bấm nhảy được, đủ phụ lục và tài liệu tham khảo.

### Bước 8. Làm tương tự cho Slide_LaTeX/slide.tex
1. Tạo project Overleaf thứ 2 tên `Slide_ASPX_Nhom3TV`.
2. Upload file `Slide_LaTeX/slide.tex` (và các file hình PDF đã chuyển đổi nếu có).
3. Menu -> **Compiler** = `pdfLaTeX`, **Main document** = `slide.tex`, bấm **Recompile** 2 lần.
4. Tải PDF về, đổi tên thành `Slide_ASPX_Nhom3TV.pdf`, kiểm tra đủ số slide, hình hiện đủ, không tràn chữ.

**Mẹo làm nhóm trên Overleaf:** bấm **Share** -> **Invite** thêm email 2 thành viên còn lại, bật **Can Edit**. Mỗi người sửa chương của mình rồi ghi chú lại để TV3 tổng hợp, tránh sửa cùng 1 dòng gây conflict.

---

## Phần B. Biên dịch local trên Windows (TeX Live/MiKTeX)

### B1. Cài đặt 1 lần

| Thành phần | Khuyên dùng | Ghi chú |
|---|---|---|
| Bộ TeX | TeX Live (đầy đủ) hoặc MiKTeX (nhẹ, tự tải gói) | Cài bản mới nhất cho Windows, chọn đầy đủ gói tiếng Việt |
| Editor | TeXstudio hoặc VS Code + extension LaTeX Workshop | TeXstudio dễ nhất cho người mới vì có nút Build sẵn |
| Công cụ phụ | Inkscape + Perl (cho `latexmk` nếu muốn) | Inkscape dùng chuyển SVG sang PDF ở Phần D |

Sau khi cài MiKTeX, mở **MiKTeX Console** -> **Updates** -> **Check for updates** -> cập nhật hết gói. Với TeX Live, mở **TeX Live Manager** và đảm bảo có các gói: `babel-vietnamese`, `vntex`, `listings`, `bibtex`, `beamer`, `pgf` (TikZ).

### B2. Biên dịch báo cáo (4 lệnh, bắt buộc theo thứ tự)

```bash
cd BaoCao_LaTeX
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Ý nghĩa từng lệnh:

| Lượt | Lệnh | Tác dụng |
|---|---|---|
| 1 | `pdflatex main.tex` | Tạo `.aux`, phát hiện citation và label nào cần xử lý |
| 2 | `bibtex main` | Đọc `.aux` + `.bib`, tạo `.bbl` chứa tài liệu tham khảo (chú ý: `bibtex main`, không có `.tex`) |
| 3 | `pdflatex main.tex` | Nhúng `.bbl` vào PDF, cập nhật citation |
| 4 | `pdflatex main.tex` | Chốt mục lục, số trang, tham chiếu chéo |

### B3. Biên dịch slide (2 lệnh)

```bash
cd Slide_LaTeX
pdflatex slide.tex
pdflatex slide.tex
```

Slide Beamer không dùng `bibtex` nên chỉ cần 2 lượt `pdflatex` để ổn định navigation và số trang.

### B4. Dọn file tạm và kiểm tra output

```bash
dir *.pdf *.log *.aux
```

File đạt yêu cầu: `main.pdf` (báo cáo) và `slide.pdf` (slide) mở được, đủ chữ tiếng Việt. Các file `.aux`, `.log`, `.toc`, `.out`, `.bbl`, `.blg` là file tạm, không nộp, chỉ giữ lại `.tex` + `.bib` + PDF. Nếu muốn biên dịch 1 lệnh duy nhất, dùng `latexmk -pdf main.tex` (báo cáo) hoặc `latexmk -pdf slide.tex` (slide).

---

## Phần C. 10 lỗi thường gặp và cách sửa

| # | Thông báo lỗi / Dấu hiệu | Nguyên nhân | Cách sửa đúng |
|---|---|---|---|
| 1 | `Font T5/cmr/m/n/10=... not loadable` hoặc mất dấu tiếng Việt | Thiếu gói `vntex`, hoặc sai thứ tự `fontenc`/`babel` | Đảm bảo preamble có đủ 3 dòng theo đúng thứ tự: `\usepackage[T5]{fontenc}`, `\usepackage[utf8]{inputenc}`, `\usepackage[vietnamese]{babel}`. Trên MiKTeX mở Console cài thêm gói `vntex` và `babel-vietnamese` rồi biên dịch lại. |
| 2 | `! Verbatim-like command \verb in section title` | Dùng `\verb` trong `\section`, `\caption`, `\footnote` (lệnh fragile) | Không dùng `\verb` trong tiêu đề. Thay bằng `\texttt{git rebase -i}` hoặc `\lstinline|git rebase -i|`. Ví dụ sai: `\section{Dung \verb|git log|}`. Ví dụ đúng: `\section{Dung \texttt{git log}}`. |
| 3 | `Label ... multiply defined` | Hai `\label` trùng tên, thường do copy-paste chương | Đặt label theo quy tắc `tiền tố:chương:tên`, ví dụ `\label{fig:c2:3vung}`, `\label{tab:c6:sosanh}`, `\label{sec:c4:actions}`. Tìm tên trùng bằng tìm kiếm `label{fig` trong toàn bộ thư mục rồi đổi tên. |
| 4 | Tài liệu tham khảo trống, log báo `Empty thebibliography` | File `.bib` rỗng, sai tên file, hoặc quên chạy `bibtex` | Kiểm tra `tailieu_thamkhao.bib` có ít nhất 1 entry `@book`/`@online`, trong `main.tex` có `\bibliography{tailieu_thamkhao}` (không ghi `.bib`) + `\bibliographystyle{plain}`. Chạy đủ 4 lệnh Phần B, không chạy `bibtex main.tex`. |
| 5 | `listings` báo lỗi với ký tự `_, #, %, &, {, }` hoặc code ASPX | Gõ ký tự đặc biệt trực tiếp trong `\lstinline` hoặc `lstlisting` chưa escape | Trong văn bản thường escape: `\_`, `\#`, `\%`, `\&`. Trong `lstlisting` đặt `literate` cho tiếng Việt và giữ nguyên code, ví dụ `literate={đ}{{\dj}}1 {ê}{{\^e}}1`. Với inline code chứa `|` thì đổi ký tự bao: `\lstinline!Web.config!`. |
| 6 | `! Undefined control sequence` tại dòng có lệnh tự định nghĩa | Gõ sai tên lệnh hoặc thiếu gói định nghĩa lệnh đó | Đọc log xem tên lệnh sau `Undefined control sequence`, ví dụ TikZ báo lỗi thì thêm `\usepackage{tikz}` và `\usetikzlibrary{arrows.meta,positioning,shapes}`. |
| 7 | Hình không hiện, báo `File ... not found` | Sai đường dẫn hình hoặc chưa chuyển SVG sang PDF | Đặt file hình cùng thư mục với `.tex` hoặc dùng `\graphicspath{{../HinhAnh/}}`. Với pdfLaTeX chỉ nhận PNG/JPG/PDF, nên chuyển SVG sang PDF theo Phần D rồi gọi `\includegraphics{hinh.pdf}`. Tên file không dấu, không khoảng trắng. |
| 8 | `! Missing $ inserted` khi gõ `C#`, `a_b`, `%` | Ký tự `_`, `^`, `#`, `%` bị hiểu là lệnh toán | Trong văn bản viết `C\#`, `a\_b`, `100\%`. Trong code thì cho vào `lstlisting` hoặc `\texttt{}` đã escape. Không bao cả đoạn văn tiếng Việt trong `$...$` để sửa lỗi này. |
| 9 | Mục lục, số hình, citation hiện `??` hoặc `[?]` | Mới biên dịch 1 lần, chưa đủ lượt | Báo cáo phải chạy đủ 4 lượt, slide 2 lượt như Phần A/B. Nếu đã chạy đủ mà vẫn `?`, xóa file tạm `.aux`, `.toc`, `.out` rồi biên dịch lại từ đầu. Trên Overleaf dùng **Clear Cached Files**. |
| 10 | `! TeX capacity exceeded` hoặc treo khi vẽ TikZ | Vòng lặp TikZ sai, node quá lớn, hoặc ảnh PDF quá nặng | Thu gọn hình TikZ: giảm số node, tách hình lớn thành 2 hình, thêm `scale=0.8, transform shape`. Nén ảnh PNG/JPG dưới 1 MB trước khi `\includegraphics`. Nếu vẫn treo, comment tạm hình bằng `%` để xác định hình nào gây lỗi rồi sửa riêng. |

**Quy trình sửa lỗi chuẩn cho người mới:** đọc 5 dòng đầu trong log đỏ -> xác định số dòng `.tex` bị lỗi -> sửa 1 lỗi -> Recompile -> nếu hết đỏ mới sửa lỗi tiếp theo. Không sửa 10 chỗ cùng lúc vì không biết chỗ nào gây lỗi.

---

## Phần D. Chuyển SVG sang PDF bằng Inkscape (để pdfLaTeX đọc được)

`pdflatex` không đọc trực tiếp file `.svg`. Nhóm có 2 cách: giữ hình TikZ có sẵn trong `.tex` (biên dịch ngay được), hoặc chuyển file trong `HinhAnh/*.svg` sang PDF rồi `\includegraphics`. Dưới đây là cách chuyển đúng cho 7 hình của nhóm.

### D1. Cài Inkscape và kiểm tra

1. Tải Inkscape bản Windows mới nhất, cài đặt bình thường, tick chọn **Add to PATH** nếu có.
2. Mở PowerShell hoặc CMD, kiểm tra:

```bash
inkscape --version
```

Nếu hiện `Inkscape 1.x` là thành công. Nếu báo không tìm thấy lệnh thì mở Inkscape bằng đường dẫn đầy đủ, ví dụ `"C:\Program Files\Inkscape\bin\inkscape.exe" --version`.

### D2. Chuyển 1 file SVG sang PDF (làm tay)

```bash
cd HinhAnh
inkscape git-3-vung.svg -o git-3-vung.pdf
```

Lệnh trên tạo `git-3-vung.pdf` nằm cạnh file `.svg`. Trong `.tex` gọi `\includegraphics[width=0.8\textwidth]{../HinhAnh/git-3-vung.pdf}` (đường dẫn tương đối từ thư mục `.tex`).

### D3. Chuyển hàng loạt cả 7 hình (khuyên dùng)

```bash
cd HinhAnh
inkscape git-3-vung.svg -o git-3-vung.pdf
inkscape git-branch-merge.svg -o git-branch-merge.pdf
inkscape gitflow.svg -o gitflow.pdf
inkscape pr-flow.svg -o pr-flow.pdf
inkscape cicd-tongquan.svg -o cicd-tongquan.pdf
inkscape cicd-github.svg -o cicd-github.pdf
inkscape cicd-gitlab.svg -o cicd-gitlab.pdf
```

Sau khi chạy, kiểm tra có đủ 7 file `.pdf` bằng lệnh `dir *.pdf`. Upload cả 7 file PDF này lên Overleaf (đặt cùng thư mục với `.tex` hoặc giữ cấu trúc `HinhAnh/` và dùng `\graphicspath`).

### D4. Lỗi Inkscape thường gặp

| Dấu hiệu | Cách sửa |
|---|---|
| `Failed to load ... .svg` | File SVG lưu sai encoding, mở bằng Inkscape rồi Save lại, hoặc mở bằng trình duyệt xem có hiện hình không |
| PDF xuất ra trắng trơn | Do layer bị ẩn, trong Inkscape bấm Ctrl+A xem có đối tượng không, kiểm tra Fill màu không để trong suốt 0% |
| Chữ trong PDF bị vỡ font | Trong Inkscape chọn text -> Path -> Object to Path trước khi export, hoặc cài đủ font dùng trong SVG |

---

## Checklist nộp bài sau khi biên dịch xong

- [ ] `main.pdf` đủ bìa + tên/MSSV 3 TV + mục lục + 8 chương + phụ lục + tài liệu tham khảo, không còn `[?]`.
- [ ] `slide.pdf` đủ slide 1-65 theo phân công, hình hiện đủ, không tràn chữ, có slide phân công + Q&A.
- [ ] Đã đổi tên file nộp: `BaoCao_ASPX_Nhom3TV.pdf`, `Slide_ASPX_Nhom3TV.pdf`, không nộp tên `main.pdf` gây nhầm.
- [ ] Source nộp kèm biên dịch lại được từ đầu: `.tex` + `.bib` + 7 PDF hình (nếu dùng `\includegraphics`).

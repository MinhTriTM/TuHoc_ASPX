# KẾ HOẠCH LÀM VIỆC, ĐẦU RA VÀ CÁC VẤN ĐỀ ĐẶT RA CHO THÀNH VIÊN 2 (TV2)

> **Mảng phụ trách:** GitHub + CI/CD cho ASPX (GitHub Actions) + Tổng hợp Slide Beamer  
> **Học phần:** Lập trình ASPX (.NET Framework 4.8.1) — Đồ án nhóm 3 thành viên  
> **Trọng số rubric:** Chiếm 3.5 / 10 điểm toàn bài (Tiêu chí 2: 2.0đ, Tiêu chí 4: 1.5đ + phần demo live).

---

## I. CÁC BƯỚC LÀM VIỆC CỤ THỂ CỦA TV2 (5 GIAI ĐOẠN)

```
[Giai đoạn 1] ──> [Giai đoạn 2] ──> [Giai đoạn 3] ──> [Giai đoạn 4] ──> [Giai đoạn 5]
  Thiết lập         Xây dựng          Soạn Báo cáo        Diễn tập           Luyện phản
  Repo & Rule       Pipeline CI       & Slide Beamer       Demo Live         biện 10 câu
```

### Giai đoạn 1: Thiết lập hạ tầng Repository & Quản trị nhóm (Ngày 1–2)
1. **Khởi tạo và cấu hình Repo:** Tạo repository trên GitHub (ví dụ `TuHoc_ASPX` hoặc `AspxDemo_NET481`), phân quyền Collaborator cho TV1 và TV3.
2. **Thiết lập bảng Projects (Kanban):** Tạo các cột `To Do`, `In Progress`, `Under Review`, `Done` để theo dõi tiến độ nhóm.
3. **Cấu hình bảo vệ nhánh (Protected Branch & Rulesets):**
   - Thiết lập bảo vệ cho nhánh `main`.
   - Bật: *Require a pull request before merging* (yêu cầu ít nhất 1 approval).
   - Bật: *Require status checks to pass before merging* (chỉ định check `CI ASPX 4.8.1`).
   - Bật: *Do not allow force pushes* và *Do not allow deletions*.
4. **Cấu hình file `CODEOWNERS`:** Phân quyền review file tự động theo đường dẫn (`*.aspx` do TV1 review, `Web.config` và `.github/` do TV2 review, `.gitlab-ci.yml` do TV3 review).
5. **Cấu hình GitHub Secrets:** Thêm các secret mẫu như `DB_CONNECTION_STRING` vào *Settings -> Secrets and variables -> Actions*.

### Giai đoạn 2: Xây dựng Pipeline GitHub Actions cho ASPX 4.8.1 (Ngày 2–3)
1. **Tạo nhánh phát triển:** Tạo nhánh `feature/github-actions` từ `main`.
2. **Soạn thảo tệp YAML workflow:** Viết file `.github/workflows/ci-aspx-481.yml` chạy trên máy ảo `windows-latest`.
3. **Hiện thực hóa 8 bước trong Job build:**
   - `actions/checkout@v4`
   - `microsoft/setup-msbuild@v2`
   - `nuget/setup-nuget@v2`
   - `actions/cache@v4` (cấu hình cache NuGet)
   - `nuget restore AspxDemo_NET481.sln`
   - `msbuild AspxDemo_NET481.sln /p:Configuration=Release`
   - Thực thi `vstest.console.exe` (nếu có dự án Test)
   - `actions/upload-artifact@v4` (đóng gói artifact web deployable)
4. **Kiểm thử và tối ưu:** Push thử nghiệm, đảm bảo pipeline báo **tích xanh (Success)** và thời gian chạy dưới 1 phút.

### Giai đoạn 3: Biên soạn Báo cáo & Tổng hợp Slide Beamer (Ngày 3–5)
1. **Viết Báo cáo LaTeX (Chương 4 & Phụ lục C.1):**
   - Hoàn thiện nội dung lý thuyết 8 tính năng cốt lõi của GitHub.
   - Bảng đối chiếu Fork vs Branch (bảng $\ge$ 5 tiêu chí).
   - Cơ chế bảo mật: Secret Scanning, Dependabot, CodeQL.
   - Viết Phụ lục C.1: Giải thích từng dòng trong file YAML mẫu.
2. **Vẽ và xuất 2 sơ đồ vector:**
   - `pr-flow.svg`: Quy trình 5 bước của Pull Request.
   - `cicd-github.svg`: Kiến trúc các bước của pipeline GitHub Actions.
3. **Tổng hợp Slide Beamer (Nhiệm vụ riêng của TV2 theo rubric):**
   - Thu thập slide từ TV1 (Phần 1, 2) và TV3 (Phần 6, 7, 8).
   - Trực tiếp soạn Phần 4 (GitHub) và Phần 5 (GitHub Actions) trong `Slide_LaTeX/`.
   - Kiểm tra biên dịch file `slide.tex` bằng `pdflatex` 2 lần, đảm bảo không còn warning, hình vẽ sắc nét, font chữ dễ đọc từ xa.

### Giai đoạn 4: Diễn tập Kịch bản Demo Live (Ngày 5–6)
1. **Chuẩn bị môi trường:** Chuẩn bị 1 PR mẫu trên nhánh `feature/dang-nhap` hoặc `feature/trang-chu`.
2. **Bấm giờ thao tác thực tế (5–7 phút):**
   - Thao tác mở PR $\rightarrow$ Chỉ ra nút Merge bị khóa $\rightarrow$ TV1 Approve $\rightarrow$ Chiếu tab Actions chạy xanh $\rightarrow$ Squash & Merge $\rightarrow$ Xóa nhánh $\rightarrow$ Mở gói Artifact.
3. **Diễn tập phương án dự phòng (Fallback plan):** Chuẩn bị sẵn tab browser có run thành công trước đó đề phòng sự cố mạng.

### Giai đoạn 5: Ôn tập Ngân hàng Câu hỏi Phản biện (Ngày 6–7)
- Học thuộc bản chất kỹ thuật và cách trả lời ngắn gọn (2–4 câu) cho 10 câu hỏi mảng GitHub (B1 – B10).

---

## II. ĐẦU RA CỤ THỂ (DELIVERABLES / DEFINITION OF DONE)

| Lĩnh vực | Hạng mục đầu ra | Tiêu chuẩn nghiệm thu (Mức Xuất sắc Rubric) |
|---|---|---|
| **Hạ tầng GitHub** | Repository GitHub chính thức của nhóm | Đầy đủ Issues mẫu, Project Board Kanban, Protected Branch, CODEOWNERS và Secrets. |
| **Mã nguồn CI/CD** | Tệp `.github/workflows/ci-aspx-481.yml` | Chạy trên `windows-latest`, có cache NuGet, build MSBuild Release pass 100% (tích xanh). |
| **Lịch sử Git** | 1 Pull Request mẫu đã hoàn thành | Mở từ nhánh feature, có comment thảo luận, có review Approve, CI xanh, merge dạng Squash và đã xóa nhánh. |
| **Đóng gói sản phẩm** | Build Artifact trên GitHub Actions | File `aspx-deployable-package.zip` được tải lên tab Actions sau mỗi lần build. |
| **Hình vẽ minh họa** | 2 sơ đồ định dạng SVG | `pr-flow.svg` và `cicd-github.svg` nhúng hiển thị rõ ràng trong báo cáo và slide. |
| **Báo cáo LaTeX** | Chương 4 + Phụ lục C.1 | Đầy đủ 8 tính năng GitHub, phân tích sâu MSBuild và Actions, biên dịch `pdflatex` không lỗi. |
| **Slide thuyết trình** | File `Slide_LaTeX/slide.pdf` | TV2 tổng hợp đạt 55–65 slide, tỉ lệ 16:9, đủ 8 phần của cả 3 thành viên, layout đồng nhất. |
| **Bảo vệ trực tiếp** | Demo live 5–7 phút + Trả lời phản biện | Demo mượt mà không lỗi thao tác, trả lời đúng $\ge$ 4/5 câu hỏi ngẫu nhiên trong nhóm B1–B10. |

---

## III. CÁC VẤN ĐỀ ĐẶT RA & GIẢI PHÁP KỸ THUẬT (PROBLEM STATEMENTS)

### Vấn đề 1: Rào cản tương thích nền tảng (Platform Incompatibility)
- **Bản chất vấn đề:** ASP.NET Web Forms (.NET Framework 4.8.1) ra đời từ trước kỷ nguyên .NET Core đa nền tảng. Nó phụ thuộc trực tiếp vào Windows GAC, IIS Metabase, thư viện `System.Web` và bộ nạp MSBuild bản đầy đủ. Sinh viên thường nhầm lẫn dùng `ubuntu-latest` hoặc lệnh `dotnet build` dẫn đến pipeline báo lỗi đỏ ngay bước đầu.
- **Giải pháp của TV2:**
  - Bắt buộc khai báo `runs-on: windows-latest`.
  - Sử dụng action chính thức `microsoft/setup-msbuild@v2` để đưa MSBuild vào biến môi trường PATH.
  - Sử dụng `nuget/setup-nuget@v2` và lệnh `nuget restore` thay vì dùng `dotnet restore`.

### Vấn đề 2: Tiêu tốn tài nguyên và nguy cơ cạn kiệt hạn ngạch (Action Quota Limit)
- **Bản chất vấn đề:** Tài khoản GitHub miễn phí chỉ có 2,000 phút Actions/tháng. Đáng chú ý, **Windows runner bị nhân hệ số 2x** (1 phút chạy máy ảo Windows = 2 phút bị trừ hạn ngạch). Nếu mỗi lần push mã nguồn, máy ảo phải tải lại hàng trăm MB gói NuGet từ Internet thì mỗi lần build mất 4–5 phút, rất nhanh cạn hạn ngạch.
- **Giải pháp của TV2:**
  - Tích hợp `actions/cache@v4` cho thư mục `~/.nuget/packages`, sử dụng khóa băm theo nội dung file cấu hình gói. Kết quả: thời gian restore giảm từ 3 phút xuống còn 10–15 giây!
  - Thiết lập khối `concurrency` với thuộc tính `cancel-in-progress: true` để tự động hủy lượt build cũ khi thành viên đẩy commit mới liên tiếp trên cùng nhánh.
  - Chuẩn bị phương án Self-Hosted Runner (cài đặt runner cục bộ trên máy tính của thành viên) nếu lớp học yêu cầu build tần suất cao.

### Vấn đề 3: Nguy cơ lộ lọt thông tin nhạy cảm (Credentials & Secret Exposure)
- **Bản chất vấn đề:** File `Web.config` trong đồ án Web Forms thường chứa chuỗi kết nối SQL Server (`connectionStrings`) bao gồm Server IP, User ID và Password. Đưa file này lên public repo là lỗ hổng bảo mật nghiêm trọng.
- **Giải pháp của TV2:**
  - Tách chuỗi kết nối ra biến bí mật **GitHub Secrets** (`${{ secrets.DB_CONNECTION }}`).
  - Bật tính năng **Secret Scanning** và **Push Protection** trong mục Security để chặn đứng commit từ máy trạm nếu có mật khẩu lọt vào code.
  - Áp dụng cơ chế cấu hình biến đổi `Web.Release.config` (XML Document Transform) khi MSBuild biên dịch chế độ Release.

### Vấn đề 4: Kỷ luật làm việc nhóm và bảo vệ nhánh chính (Branch Governance)
- **Bản chất vấn đề:** Trong nhóm 3 sinh viên, chỉ cần 1 thành viên sơ suất gõ lệnh `git push --force origin main` hoặc commit code bị lỗi cú pháp thẳng lên nhánh chính thì toàn bộ bài làm sẽ bị hỏng, mất lịch sử và không thể demo trước giảng viên.
- **Giải pháp của TV2:**
  - Khóa hoàn toàn quyền push trực tiếp lên nhánh `main` thông qua **Protected Branch Rules** và **GitHub Rulesets**.
  - Thiết lập rào chắn bắt buộc 2 cổng kiểm tra: (1) Cổng con người: Tối thiểu 1 thành viên review Approve; (2) Cổng tự động: Pipeline CI build pass tích xanh mới được mở nút Merge.
  - Cấu hình file `CODEOWNERS` để quy trách nhiệm duyệt mã nguồn rõ ràng cho từng thành viên.

### Vấn đề 5: Rủi ro kỹ thuật trong quá trình Demo Live trước hội đồng
- **Bản chất vấn đề:** Khi demo trực tiếp, phòng học có thể bị nghẽn mạng WiFi, hệ thống GitHub Actions gặp tình trạng quá tải (trạng thái Queued kéo dài vài phút), hoặc thao tác tay bị vấp dẫn đến quá thời lượng 5–7 phút.
- **Giải pháp của TV2:**
  - Chuẩn bị kịch bản "2 màn hình": Mở sẵn 1 tab có PR đang chạy thực tế, và 1 tab dự phòng có workflow gần nhất đã chạy xanh hoàn hảo kèm tệp artifact đã tải sẵn.
  - Thực hiện diễn tập bấm giờ (dry run) ít nhất 2 lần trước ngày bảo vệ.
  - Nắm chắc 10 câu hỏi phản biện B1–B10 để biến mọi câu hỏi vặn vẹo của giảng viên thành cơ hội ghi trọn điểm Xuất sắc (2.0/2.0).

# TÀI LIỆU VÀ KỊCH BẢN TRÌNH BÀY: TV2 — GITHUB + CI/CD CHO ASPX (.NET FRAMEWORK 4.8.1)

> **Dành cho:** Thành viên TV2 (Phụ trách GitHub + Actions CI/CD)  
> **Học phần:** Lập trình ASPX (.NET Framework 4.8.1)  
> **Không gian lưu trữ:** [Github_kiet](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/Github_kiet)  
> **Nguồn đối chiếu:** [Chương 4 Báo cáo](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/BaoCao_LaTeX/chuong4-1-github-coban.tex), [Slide Phần 4 & 5](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/Slide_LaTeX/phan4-github.tex), [Phụ lục C.1](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/BaoCao_LaTeX/phulucC-yaml.tex), [Kịch bản thuyết trình](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/KichBan_ThuyetTrinh.md).

---

## MỤC LỤC
1. [Mục tiêu và Tiêu chí Đạt (Definition of Done)](#1-mục-tiêu-và-tiêu-chí-đạt)
2. [Hệ thống 8 Tính Năng Cốt Lõi của GitHub](#2-hệ-thống-8-tính-năng-cốt-lõi-của-github)
3. [Chuyên đề Sâu: GitHub Actions CI/CD cho ASP.NET Web Forms 4.8.1](#3-chuyên-đề-sâu-github-actions-cicd-cho-aspnet-web-forms-481)
4. [Bảo Mật Dự Án: Protected Branch, Secrets, CODEOWNERS và Security Suite](#4-bảo-mật-dự-án)
5. [Kịch Bản Thuyết Trình Chi Tiết Từng Phút (7 phút nói + 5-7 phút demo live)](#5-kịch-bản-thuyết-trình-chi-tiết)
6. [Kịch Bản Demo Live Chi Tiết Từng Bước](#6-kịch-bản-demo-live-chi-tiết-từng-bước)
7. [Ngân Hàng 10 Câu Hỏi Phản Biện Mở Rộng (B1 – B10) & Gợi Ý Trả Lời Chuẩn](#7-ngân-hàng-10-câu-hỏi-phản-biện)

---

## 1. MỤC TIÊU VÀ TIÊU CHÍ ĐẠT

| Hạng mục | Nhiệm vụ của TV2 | Đầu ra thực tế |
|---|---|---|
| **Báo cáo** | Chương 4 (GitHub toàn diện) + Phụ lục C.1 (YAML mẫu) | Đầy đủ nội dung trong [chuong4-*.tex](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/BaoCao_LaTeX/) |
| **Slide** | Phần 3 (Khoảng slide 26–45, tương ứng phần 4 và 5) | Đầy đủ khung trong [phan4-github.tex](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/Slide_LaTeX/phan4-github.tex) & [phan5-github-actions.tex](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/Slide_LaTeX/phan5-github-actions.tex) |
| **Hình vẽ minh họa** | Phụ trách vẽ và giải thích 2 sơ đồ vector | `pr-flow.svg` (luồng PR) và `cicd-github.svg` (pipeline Actions) |
| **Repo Demo** | Dựng nhánh `feature/github-actions` | File `.github/workflows/ci-aspx-481.yml` build pass (xanh 100%) |
| **Demo Live (5–7p)** | Thao tác thực tế trước hội đồng | Mở PR $\rightarrow$ Review/Approve $\rightarrow$ Actions chạy $\rightarrow$ Merge |
| **Tiêu chí đạt** | 8 tính năng GitHub + Pipeline xanh + Phản biện vững | Nắm chắc lý thuyết, thực hành và xử lý tình huống phản biện |

---

## 2. HỆ THỐNG 8 TÍNH NĂNG CỐT LÕI CỦA GITHUB

Khi trình bày hoặc trả lời phản biện, TV2 cần làm bật lên sự khác biệt: **"Git là công cụ theo dõi phiên bản phân tán trên máy cá nhân, còn GitHub là nền tảng điện toán đám mây và cộng tác toàn diện xoay quanh Git"**.

```
                           HỆ SINH THÁI GITHUB
 ┌────────────────────────────────────────────────────────────────────────┐
 │ 1. Issues & Projects  ── Quản lý công việc, Kanban, phân chia Task     │
 │ 2. Pull Requests (PR) ── Cốt lõi review code, thảo luận, bảo vệ nhánh  │
 │ 3. GitHub Actions     ── Tự động hóa CI/CD, build MSBuild cho ASPX     │
 │ 4. GitHub Packages    ── Kho lưu trữ gói thư viện nội bộ (.nupkg)      │
 │ 5. GitHub Pages       ── Hosting tài liệu đồ án, web tĩnh miễn phí     │
 │ 6. GitHub Security    ── Secret Scanning, Dependabot, CodeQL (SAST)    │
 │ 7. GitHub Codespaces  ── Môi trường lập trình Dev Container trên Cloud │
 │ 8. GitHub Copilot     ── Trợ lý AI hỗ trợ viết C#, Regex, ASPX tag     │
 └────────────────────────────────────────────────────────────────────────┘
```

### 1. Issues & Projects (Quản trị tiến độ nhóm)
- **Issues:** Nơi theo dõi lỗi (bug), tính năng mới (feature request) hoặc công việc cần làm.
  - Mỗi Issue có: Title, Description (theo template), Assignees (thành viên chịu trách nhiệm), Labels (`bug`, `enhancement`, `documentation`), Milestone (mốc đồ án).
  - Tự động hóa liên kết commit/PR: Viết `Fixes #12` hoặc `Closes #12` trong PR description sẽ tự động đóng Issue #12 khi PR được merge.
- **Projects:** Bảng Kanban (Todo $\rightarrow$ In Progress $\rightarrow$ Review $\rightarrow$ Done) trực quan hóa tiến độ nhóm 3 người mà không cần phần mềm thứ ba như Trello hay Jira.

### 2. Pull Requests (PR - Quy trình cộng tác hạt nhân)
- Không ai được phép push code thẳng vào `main` hay `develop`.
- Mọi tính năng (trang `Login.aspx`, `Default.aspx`) đều làm trên nhánh `feature/...`, sau đó mở Pull Request so sánh diff giữa nhánh tính năng và nhánh đích.
- Hỗ trợ inline code review: thành viên khác có thể bôi đen từng dòng code để comment, gợi ý sửa đổi (`Suggest change`), bắt buộc sửa trước khi bấm **Approve**.

### 3. GitHub Actions (Tự động hóa CI/CD)
- Hệ thống tự động kích hoạt workflow khi có sự kiện (`push`, `pull_request`).
- Giúp kiểm chứng mã nguồn độc lập trên máy ảo: Đảm bảo code tải về máy nào cũng build được, loại bỏ hoàn toàn câu nói *"Trên máy em vẫn chạy bình thường"*.

### 4. GitHub Packages (Quản lý thư viện phụ thuộc nội bộ)
- Dành cho các nhóm muốn chia sẻ thư viện dùng chung (như thư viện mã hóa mật khẩu SHA256, lớp kết nối CSDL ADO.NET) dưới dạng gói **NuGet (`.nupkg`)**.
- Máy chủ package: `https://nuget.pkg.github.com/OWNER/index.json`. Bảo mật bằng `GITHUB_TOKEN`.

### 5. GitHub Pages (Xuất bản tài liệu dự án)
- Hosting trang web tĩnh miễn phí trực tiếp từ thư mục `docs/` hoặc nhánh `gh-pages`.
- Nhóm dùng Pages để đưa sơ đồ ERD, tài liệu hướng dẫn cài đặt, báo cáo nghiệm thu lên đường link công khai: `https://<user>.github.io/<repo-name>/`.

### 6. GitHub Security (An ninh mã nguồn tự động)
- **Secret Scanning:** Quét phát hiện lộ mật khẩu, Access Token hoặc Connection String SQL Server trong commit. Tính năng **Push Protection** sẽ chặn đứng lệnh push nếu phát hiện chuỗi secret.
- **Dependabot:** Tự động phát hiện các gói NuGet có lỗ hổng bảo mật đã biết (CVE), tự động tạo PR nâng cấp phiên bản an toàn.
- **CodeQL:** Công cụ quét mã tĩnh (SAST) do GitHub phát triển, tìm kiếm lỗi bảo mật trong code C# như SQL Injection, Cross-Site Scripting (XSS), Insecure Deserialization.

### 7. GitHub Codespaces (IDE trên đám mây)
- Cung cấp container Linux cấu hình sẵn VS Code trên trình duyệt.
- Dù Web Forms 4.8.1 cần Windows để build hoàn chỉnh, Codespaces là giải pháp tuyệt vời để thành viên sửa code nhanh, viết báo cáo LaTeX, chỉnh sửa tài liệu hoặc review PR từ bất kỳ thiết bị nào (kể cả máy tính bảng hoặc Chromebook).

### 8. GitHub Copilot (Trợ lý lập trình AI)
- Gợi ý code C# thông minh, tự động sinh các đoạn kiểm tra dữ liệu đầu vào trong sự kiện `btnLogin_Click`, gợi ý cấu trúc thẻ `<asp:TextBox>`, `<asp:GridView>` và giải thích các mã lỗi của MSBuild.

---

## 3. CHUYÊN ĐỀ SÂU: GITHUB ACTIONS CI/CD CHO ASP.NET WEB FORMS 4.8.1

### 3.1. Năm thành phần cốt lõi của GitHub Actions
1. **Workflow:** Tệp YAML đặt tại `.github/workflows/ci-aspx-481.yml`.
2. **Trigger (`on`):** Sự kiện kích hoạt (Ví dụ: `push`, `pull_request` vào `main`, `develop`, hoặc `workflow_dispatch`).
3. **Jobs:** Các tác vụ lớn trong workflow (chạy song song theo mặc định, hoặc nối tiếp nhau thông qua `needs`).
4. **Runner (`runs-on`):** Máy ảo chạy job. **Bắt buộc dùng `windows-latest`** cho đồ án ASPX .NET Framework 4.8.1.
5. **Steps:** Chuỗi các bước tuần tự trong job (`uses` để gọi Action dựng sẵn từ Marketplace, hoặc `run` để gõ lệnh PowerShell/cmd).

### 3.2. Vì sao ASP.NET 4.8.1 bắt buộc dùng `windows-latest`?
> [!IMPORTANT]
> **Điểm mấu chốt khi thuyết trình & bảo vệ:**
> - `.NET Core` hay `.NET 5/6/7/8` là đa nền tảng, có thể build bằng `dotnet build` trên Linux/macOS.
> - Nhưng **ASP.NET Web Forms (.NET Framework 4.8.1)** phụ thuộc sâu vào hệ điều hành Windows:
>   1. Cần trình biên dịch **MSBuild đầy đủ** (đi kèm Visual Studio Build Tools).
>   2. Cần các thư viện COM, GDI+, IIS Metabase và các assembly chuẩn của .NET Framework chỉ có sẵn trên Windows.
>   3. Lệnh `dotnet build` trên runner `ubuntu-latest` **không thể** biên dịch file `.sln` của ASP.NET Web Forms cổ điển.
> - Runner `windows-latest` của GitHub Actions đã tích hợp sẵn Visual Studio Enterprise, MSBuild, .NET Framework 4.8.1 SDK và NuGet CLI.

### 3.3. Tệp Workflow mẫu chuẩn hoàn chỉnh (`.github/workflows/ci-aspx-481.yml`)

```yaml
name: CI ASPX 4.8.1

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  workflow_dispatch:

concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true

jobs:
  build:
    name: Build & Test ASP.NET 4.8.1
    runs-on: windows-latest

    steps:
      # Bước 1: Kéo mã nguồn về máy ảo
      - name: Checkout code
        uses: actions/checkout@v4

      # Bước 2: Thiết lập đường dẫn MSBuild vào PATH
      - name: Setup MSBuild
        uses: microsoft/setup-msbuild@v2

      # Bước 3: Cài đặt công cụ NuGet CLI
      - name: Setup NuGet
        uses: nuget/setup-nuget@v2

      # Bước 4: Tối ưu tốc độ với Cache NuGet
      - name: Cache NuGet packages
        uses: actions/cache@v4
        with:
          path: ~/.nuget/packages
          key: nuget-${{ runner.os }}-${{ hashFiles('**/packages.config') }}
          restore-keys: |
            nuget-${{ runner.os }}-

      # Bước 5: Khôi phục toàn bộ các gói thư viện phụ thuộc
      - name: Restore NuGet packages
        run: nuget restore AspxDemo_NET481.sln

      # Bước 6: Biên dịch Solution ở chế độ Release
      - name: Build Solution
        run: msbuild AspxDemo_NET481.sln /p:Configuration=Release /p:DeployOnBuild=true /p:WebPublishMethod=Package /p:PackageAsSingleFile=true /p:PackageLocation="build_output\package.zip"

      # Bước 7: Thực thi kiểm thử tự động (Unit Tests)
      - name: Run Unit Tests
        run: |
          if (Test-Path "**\bin\Release\*Tests.dll") {
            vstest.console.exe (Get-ChildItem -Path . -Recurse -Filter "*Tests.dll" | Select-Object -ExpandProperty FullName)
          } else {
            Write-Host "Chua co du an Tests, bo qua buoc chay kiem thu don vi."
          }

      # Bước 8: Lưu trữ kết quả build làm Artifact
      - name: Upload Build Artifact
        uses: actions/upload-artifact@v4
        with:
          name: aspx-deployable-package
          path: build_output/
          retention-days: 7
```

---

## 4. BẢO MẬT DỰ ÁN

### 4.1. Protected Branch & Branch Rulesets
Nhánh `main` là nhánh nguồn chân lý dùng để nộp bài và chấm điểm. Phải thiết lập các rào chắn:
1. **Require a pull request before merging:** Chặn hoàn toàn lệnh `git push origin main`.
2. **Require approvals:** Bắt buộc tối thiểu 1 thành viên khác (TV1 hoặc TV3) kiểm tra và bấm nút Approve.
3. **Require status checks to pass before merging:** Bắt buộc job `Build & Test ASP.NET 4.8.1` của GitHub Actions phải báo tích xanh. Nếu code gãy build $\rightarrow$ Nút Merge bị xám, không cho gộp!
4. **Do not allow bypassing the above settings:** Áp dụng cho cả trưởng nhóm / Admin repo.

### 4.2. File `CODEOWNERS`
Tự động gắn người phụ trách review tương ứng khi PR chạm vào file cụ thể:
```text
# Toàn bộ file .aspx và giao diện do TV1 review
*.aspx @nhom3/tv1-lead
*.master @nhom3/tv1-lead

# Cấu hình Web.config và backend do TV2 review
Web.config @nhom3/tv2-devops
Web.*.config @nhom3/tv2-devops

# Hạ tầng CI/CD do TV2 quản lý
.github/workflows/ @nhom3/tv2-devops
```

### 4.3. Quản lý Connection String & GitHub Secrets
- **Quy tắc vàng:** Tuyệt đối không commit chuỗi kết nối chứa mật khẩu cơ sở dữ liệu (`Data Source=...;User ID=sa;Password=...`) vào file `Web.config` trên Git!
- **Giải pháp:**
  1. Trong repository: Lưu trữ file `Web.template.config` hoặc cấu hình `Web.Release.config` có chứa token thay thế.
  2. Trên GitHub: Vào **Settings $\rightarrow$ Secrets and variables $\rightarrow$ Actions**, tạo secret mang tên `DB_CONNECTION_STRING`.
  3. Giá trị của Secret được mã hóa 2 chiều, khi chạy pipeline trong log sẽ tự động bị che bằng chuỗi `***`.

---

## 5. KỊCH BẢN THUYẾT TRÌNH CHI TIẾT
*(Tổng thời gian trình bày lý thuyết: 7 phút)*

### Phút 0 – 1: Chuyển tiếp & Giới thiệu tổng quan GitHub
- **Lời nói:** *"Kính thưa Thầy/Cô và các bạn, vừa rồi bạn TV1 đã trình bày chi tiết về Git trên môi trường local và cấu trúc bên trong của Git. Tuy nhiên, nếu chỉ dừng lại ở local Git thì việc làm việc nhóm 3 người sẽ gặp khó khăn trong chia sẻ code, kiểm tra chất lượng và tích hợp hệ thống. Đó là lý do chúng ta cần đến **GitHub** — nền tảng cộng tác và tự động hóa phát triển phần mềm."*
- **Slide chiếu:** Slide tổng quan 8 tính năng của GitHub.
- **Điểm nhấn:** Khẳng định GitHub không chỉ là nơi lưu code, mà là một môi trường DevOps khép kín từ khâu quản lý Task (Issues/Projects) đến kiểm soát code (PR), tự động hóa (Actions) và bảo mật (Security).

### Phút 1 – 2.5: Quy trình Pull Request (PR) & Cơ chế kiểm soát
- **Lời nói:** *"Trọng tâm của làm việc nhóm trên GitHub là quy trình **Pull Request**. Nhóm chúng em tuyệt đối cấm push code thẳng lên nhánh `main`. Khi một thành viên phát triển xong chức năng (ví dụ trang `Login.aspx`), bạn ấy sẽ đẩy lên nhánh `feature/dang-nhap` và mở một Pull Request về `develop` hoặc `main`."*
- **Slide chiếu:** Sơ đồ `pr-flow.svg` (5 bước: Push nhánh $\rightarrow$ Mở PR $\rightarrow$ Review code $\rightarrow$ CI xanh $\rightarrow$ Merge).
- **Điểm nhấn:** Nhấn mạnh tính năng **Protected Branch** kết hợp **CODEOWNERS**. Code chỉ được gộp khi có sự đồng thuận của đồng đội và khi hệ thống kiểm tra tự động xác nhận code hoàn toàn không có lỗi.

### Phút 2.5 – 4.5: GitHub Actions CI/CD cho ASP.NET Web Forms 4.8.1
- **Lời nói:** *"Điểm sáng kỹ thuật quan trọng nhất trong phần của em là hệ thống tích hợp liên tục **GitHub Actions** được thiết kế riêng cho đồ án ASP.NET Web Forms 4.8.1."*
- **Slide chiếu:** Sơ đồ `cicd-github.svg` và cấu trúc file YAML.
- **Điểm nhấn:** Phân tích vì sao bắt buộc dùng `windows-latest` (do MSBuild và .NET Framework cổ điển không chạy được trên Linux). Trình bày cách nhóm tối ưu hóa tốc độ build từ 4 phút xuống dưới 1 phút bằng kỹ thuật **Cache NuGet packages**.

### Phút 4.5 – 6: Hệ thống Bảo Mật & Các tính năng mở rộng
- **Lời nói:** *"Bên cạnh CI/CD, GitHub cung cấp bộ công cụ bảo mật toàn diện. Nhóm em đã bật **Secret Scanning** để bảo vệ chuỗi kết nối CSDL trong file `Web.config`, **Dependabot** để tự động quét lỗ hổng các thư viện NuGet bên thứ ba, và **CodeQL** để phân tích mã tĩnh C# phòng ngừa lỗi SQL Injection."*
- **Slide chiếu:** Slide Security, Packages, Pages, Codespaces và Copilot.

### Phút 6 – 7: Tóm tắt & Chuyển sang phần Demo Live
- **Lời nói:** *"Tóm lại, GitHub đã giúp nhóm chuẩn hóa toàn bộ quy trình: code sạch, tự động kiểm thử và an toàn thông tin. Ngay sau đây, em xin phép bước vào phần **Demo Live** trực tiếp trên repository của nhóm để minh họa quy trình từ lúc mở Pull Request đến khi pipeline CI chạy xanh và merge code."*

---

## 6. KỊCH BẢN DEMO LIVE CHI TIẾT TỪNG BƯỚC
*(Thời gian: 5–7 phút thực chiến)*

### Chuẩn bị trước khi demo:
- Tab 1: Repo GitHub của nhóm, đang đứng tại trang Pull Requests.
- Tab 2: Tab Actions sẵn sàng hiển thị danh sách workflow.
- Tab 3: Visual Studio hoặc Git Bash trên máy cá nhân có sẵn nhánh `feature/github-actions` với một thay đổi nhỏ (ví dụ: bổ sung chú thích hoặc sửa tiêu đề trên `Default.aspx`).

### Trình tự 6 bước thao tác:
1. **Bước 1 — Đẩy code & Mở PR:**
   - Trên Git Bash gõ: `git push origin feature/github-actions`.
   - Trên trình duyệt mở GitHub, xuất hiện thông báo *"Compare & pull request"*. Bấm tạo PR với tiêu đề: `feat(ui): cap nhat giao dien trang chu Default.aspx`.
   - Trong phần mô tả gõ: `Closes #5. Kèm thay đổi kiểm tra pipeline CI.`.
2. **Bước 2 — Trình diễn Protected Branch Rules:**
   - Cuộn xuống phần kiểm tra bên dưới PR: Chỉ cho hội đồng thấy nút **Merge pull request** đang bị **vô hiệu hóa (xám)**.
   - Giải thích: *"Hệ thống đang chặn merge vì 2 điều kiện: (1) Cần tối thiểu 1 Approve từ Reviewer; (2) Job CI trên Windows đang chạy kiểm tra."*
3. **Bước 3 — Review Code & Approve:**
   - Nhờ TV1 hoặc mở tài khoản thứ 2 vào tab **Files changed**.
   - Review qua diff của file `.aspx` và `.yml`, để lại bình luận và chọn **Approve**.
4. **Bước 4 — Quan sát Pipeline GitHub Actions:**
   - Chuyển sang tab Actions, bấm vào workflow `CI ASPX 4.8.1` đang chạy.
   - Giải thích từng step đang diễn ra theo thời gian thực: `Setup MSBuild` $\rightarrow$ `NuGet restore (Cache Hit)` $\rightarrow$ `MSBuild Release` $\rightarrow$ `Upload Artifact`.
   - Nhấn mạnh: Pipeline hoàn thành chỉ mất khoảng 40–50 giây và hiện **dấu tích xanh**.
5. **Bước 5 — Hoàn tất Merge & Dọn dẹp nhánh:**
   - Quay lại trang PR: Lúc này nút **Merge pull request** đã chuyển sang **màu xanh lục**.
   - Bấm chọn **Squash and merge** để giữ lịch sử commit của nhánh chính luôn gọn gàng.
   - Bấm **Delete branch** để xóa nhánh tính năng sau khi đã hoàn thành.
6. **Bước 6 — Kiểm chứng Artifact:**
   - Mở bản build trong tab Actions, chỉ ra tệp `aspx-deployable-package.zip` đã được tự động đóng gói sẵn sàng để deploy lên IIS.

---

## 7. NGÂN HÀNG 10 CÂU HỎI PHẢN BIỆN (B1 – B10) & GỢI Ý TRẢ LỜI

### Câu B1: Fork khác Branch ở điểm nào? Vì sao đồ án nhóm 3 người dùng Branch + PR thay vì Fork?
- **Trả lời:**
  - `Branch` là phân nhánh làm việc ngay trong cùng một kho chứa, dùng chung danh sách Issues, Projects và hạn ngạch Actions runner.
  - `Fork` là hành động nhân bản hoàn toàn một kho chứa sang tài khoản cá nhân khác, thường dùng cho cộng đồng mã nguồn mở khi người đóng góp không có quyền ghi (write permission) vào repo gốc.
  - Nhóm 3 người là cộng tác viên chính thức (collaborators), có chung mục tiêu đồ án nên sử dụng **Branch + PR** trong cùng một repo để dễ quản lý tập trung, chia sẻ Secrets và dùng chung một luồng CI/CD mà không phải cấu hình lại trên từng fork.

### Câu B2: Protected Branch kết hợp Required Review và Status Check chặn được những lỗi gì trong đồ án ASPX?
- **Trả lời:**
  - Chặn lỗi con người vô tình chạy `git push -f origin main` làm mất lịch sử của đồng đội.
  - Chặn các commit chưa hoàn chỉnh, thiếu file `.aspx.designer.cs` hoặc vỡ cú pháp C#.
  - Chặn lỗi xung đột cấu hình trong `Web.config`.
  - Nhờ Status Check, nếu code không thể biên dịch thành công bằng MSBuild trên máy ảo thì tuyệt đối không thể merge vào nhánh nộp bài.

### Câu B3: Vì sao GitHub Actions build project ASP.NET Web Forms 4.8.1 cần runner Windows? Vì sao không dùng `ubuntu-latest` + `dotnet build`?
- **Trả lời:**
  - ASP.NET Web Forms (.NET Framework 4.8.1) là công nghệ gắn liền với Windows, yêu cầu bộ biên dịch MSBuild đầy đủ của Visual Studio và các assembly hệ thống thuộc GAC của Windows.
  - `ubuntu-latest` chỉ hỗ trợ .NET Core / .NET hiện đại. Lệnh `dotnet build` trên Linux không thể hiểu các cấu trúc project Web Forms cũ, không biên dịch được các file `.aspx` và thiếu bộ nạp `System.Web`.

### Câu B4: Secrets trong Actions khác biến môi trường thường ở điểm nào? Connection string lưu ở đâu?
- **Trả lời:**
  - Biến môi trường thường (`vars`) lưu trữ công khai dưới dạng plain text và hiển thị trong log.
  - `Secrets` được GitHub mã hóa bằng khóa công khai (NaCl public-key cryptography), chỉ được giải mã trong bộ nhớ của máy ảo runner khi chạy step, và tự động bị mặt nạ hóa thành `***` nếu in ra log màn hình.
  - Chuỗi Connection String phải được lưu tại **Settings $\rightarrow$ Secrets $\rightarrow$ Actions** với tên biến (ví dụ `DB_CONN`), tuyệt đối không được lưu trong `Web.config` trên repo.

### Câu B5: Trình bày chiến lược Cache NuGet packages để tối ưu tốc độ CI?
- **Trả lời:**
  - Mỗi lần chạy mới, runner là máy ảo trắng, nếu phải tải lại hàng trăm MB gói NuGet (`Newtonsoft.Json`, `EntityFramework`, `Microsoft.AspNet.Web.Optimization`) sẽ tốn nhiều phút và băng thông.
  - Nhóm sử dụng action `actions/cache@v4` với khóa `key: nuget-${{ runner.os }}-${{ hashFiles('**/packages.config') }}`. Khi file `packages.config` không thay đổi, hệ thống sẽ khôi phục thư mục cache ngay lập tức, rút ngắn thời gian build từ 3–4 phút xuống còn dưới 1 phút.

### Câu B6: Mô tả quy trình Pull Request chuẩn của nhóm từ lúc tạo nhánh đến khi merge?
- **Trả lời:**
  1. Tạo nhánh tính năng chuẩn tên: `git checkout -b feature/ten-chuc-nang`.
  2. Thực hiện các commit tuân thủ quy ước Conventional Commits (`feat:`, `fix:`).
  3. Đẩy nhánh lên GitHub: `git push -u origin feature/...`.
  4. Mở PR trên giao diện web, điền mô tả, gắn nhãn và gán Reviewer.
  5. Đợi hệ thống GitHub Actions kiểm tra tự động (báo xanh).
  6. Reviewer xem diff, nhận xét và bấm **Approve**.
  7. Trưởng nhóm hoặc tác giả bấm **Squash and merge** và tiến hành xóa nhánh tính năng.

### Câu B7: File `CODEOWNERS` và Rulesets trong GitHub có tác dụng gì?
- **Trả lời:**
  - `CODEOWNERS` định nghĩa quyền sở hữu code theo từng thư mục. Khi một PR làm thay đổi file thuộc phạm vi đó, GitHub sẽ tự động yêu cầu review từ người sở hữu tương ứng (ví dụ: sửa file `.yml` bắt buộc TV2 duyệt).
  - `Rulesets` là bản nâng cấp mạnh mẽ hơn của Protected Branch, cho phép quản lý chính sách bảo vệ trên nhiều nhánh cùng lúc theo biểu thức quy tắc (pattern), thiết lập điều kiện bypass rõ ràng theo từng vai trò.

### Câu B8: Khi PR báo Conflict ở file cấu hình hoặc mã nguồn thì giải quyết thế nào?
- **Trả lời:**
  - Tuyệt đối không cố merge trên web khi chưa hiểu rõ xung đột.
  - Quy trình giải quyết chuẩn:
    1. Trên máy local, chuyển về nhánh feature và kéo code mới nhất từ nhánh chính: `git pull origin main`.
    2. Visual Studio hoặc VS Code sẽ đánh dấu các đoạn xung đột giữa `<<<<<<<`, `=======` và `>>>>>>>`.
    3. Thảo luận với người sửa trước để chọn cấu hình đúng nhất (ví dụ giữ connection string chuẩn hoặc gộp các thẻ cấu hình mới).
    4. Lưu file, biên dịch thử bằng MSBuild để xác nhận hết lỗi.
    5. Gõ `git add .`, commit và push lại lên nhánh feature. PR trên GitHub sẽ tự động cập nhật và chuyển sang trạng thái sẵn sàng merge.

### Câu B9: Dependabot và Secret Scanning trong GitHub Advanced Security giúp ích gì cho đồ án ASPX?
- **Trả lời:**
  - Đồ án ASPX 4.8.1 thường sử dụng nhiều thư viện NuGet cũ. **Dependabot** tự động đối chiếu danh sách gói trong `packages.config` với cơ sở dữ liệu lỗ hổng bảo mật GitHub Advisory Database. Khi phát hiện thư viện bị lỗi CVE, nó sẽ tự động mở PR đề xuất nâng cấp lên phiên bản an toàn.
  - **Secret Scanning** bảo vệ nhóm khỏi rủi ro lộ tài khoản CSDL SQL Server hoặc mật khẩu mail SMTP khi vô tình commit các file cấu hình.

### Câu B10: Nếu GitHub Actions runner `windows-latest` bị lỗi timeout hoặc hết hạn ngạch thì xử trí thế nào?
- **Trả lời:**
  - Nếu hết hạn ngạch phút miễn phí (2,000 phút/tháng cho tài khoản free, lưu ý Windows runner tính hệ số 2x phút):
    1. Nhóm có thể thiết lập **Self-Hosted Runner**: Cài đặt ứng dụng GitHub Actions Runner lên chính một máy tính Windows của thành viên trong nhóm để làm máy build riêng hoàn toàn miễn phí và tốc độ cực nhanh.
    2. Tối ưu hóa workflow bằng cách đặt thời gian timeout hợp lý (`timeout-minutes: 10`) và cấu hình `concurrency` để tự động hủy các lượt build cũ khi có commit mới được đẩy lên liên tiếp.

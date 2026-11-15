# TÀI LIỆU KỸ THUẬT CHUẨN MICROSOFT LEARN: ASP.NET WEB FORMS (.NET 4.8.1), MSBUILD & NUGET

Tài liệu này tổng hợp các chuẩn kỹ thuật cốt lõi từ Microsoft Learn (.NET Framework 4.8.1, IIS 10, MSBuild, NuGet) phục vụ việc đối chiếu và thẩm định kiến trúc trong báo cáo đồ án.

---

## 1. Cấu trúc thư mục hệ thống ASP.NET Web Forms & Bảo vệ IIS
*Nguồn tham chiếu: Microsoft Learn — ASP.NET Web Project Folder Structure; IIS Request Filtering & HttpForbiddenHandler.*

### 1.1 Thư mục `App_Data` (Bắt buộc dùng dấu gạch dưới `_`)
- **Cơ chế hoạt động**: Thư mục `App_Data` là thư mục đặc biệt được quy định bởi ASP.NET. Theo cấu hình mặc định trong `machine.config` và `root web.config` của IIS, mọi yêu cầu HTTP từ trình duyệt gửi tới thư mục có tiền tố `App_Data` đều bị chặn tự động bởi module `System.Web.HttpForbiddenHandler` (HTTP Error 403.14 - Access Denied).
- **Mục đích**: Lưu trữ cơ sở dữ liệu tệp cục bộ (`.mdf` của Microsoft SQL Server Express / LocalDB, `.xml`, tệp cấu hình nội bộ).
- **Nguy cơ khi sai tên (`App-Data`)**: IIS chỉ nhận diện chính xác xâu ký tự `App_Data`. Nếu đặt tên là `App-Data` (dấu gạch ngang), IIS sẽ coi đây là thư mục tệp tĩnh (Static Content Directory) thông thường. Khi đó, kẻ tấn công hoặc bất kỳ người dùng nào truy cập URL dạng `http://localhost/App-Data/Database.mdf` đều có thể tải toàn bộ tệp cơ sở dữ liệu về máy.

### 1.2 Thư mục `App_Code` (Bắt buộc dùng dấu gạch dưới `_`)
- **Cơ chế hoạt động**: ASP.NET Runtime tự động giám sát thư mục `App_Code` và kích hoạt trình biên dịch động (Dynamic CodeDom Compilation) để biên dịch các lớp C# (`.cs`) bên trong thành một assembly động trước khi ứng dụng thực thi.
- **Nguy cơ khi sai tên (`App-Code`)**: Nếu đặt tên `App-Code`, các file C# bên trong sẽ không được ASP.NET tự động biên dịch, dẫn đến lỗi biên dịch `CS0246: The type or namespace name '...' could not be found`.

### 1.3 Tệp cấu hình `Web.config`
- Chứa chuỗi kết nối (`<connectionStrings>`), thẻ xác thực (`<authentication>`), phân quyền URL (`<authorization>`), và chuyển hướng hợp nhất assembly (`<assemblyBinding>` / `<bindingRedirect>`).
- Bị IIS chặn truy cập trực tiếp tự động qua `HttpForbiddenHandler`.

---

## 2. MSBuild và Web Publishing Pipeline (WPP) cho ASP.NET Web Forms
*Nguồn tham chiếu: Microsoft Learn — Web Publishing Pipeline for Web Applications; MSBuild Command Line Reference.*

### 2.1 Bản chất Web Application Project (WAP) vs Class Library
- Dự án ASP.NET Web Forms (.NET 4.8.1) kế thừa từ WAP (`Microsoft.WebApplication.targets`).
- Khi chạy lệnh build thông thường:
  ```powershell
  msbuild AspxDemo.sln /p:Configuration=Release /p:Platform="Any CPU"
  ```
  MSBuild chỉ biên dịch các tệp `.cs` thành `.dll` trong thư mục `bin\`. Quá trình này **KHÔNG** đóng gói trang giao diện (`.aspx`, `.ascx`), tệp tĩnh (`.css`, `.js`, `Images/`) hay cấu hình chuyển đổi (`Web.Release.config`).

### 2.2 Các cờ bắt buộc để đóng gói ứng dụng web (Deploy on Build)
Để kích hoạt Web Publishing Pipeline sinh ra gói artifact hoàn chỉnh cho CI/CD:
```powershell
msbuild AspxDemo.sln /p:Configuration=Release `
  '/p:Platform="Any CPU"' `
  /p:DeployOnBuild=true `
  /p:WebPublishMethod=FileSystem `
  /p:PublishUrl="T:\Output\ReleaseWebPackage" `
  /p:DeleteExistingFiles=True
```
- `/p:DeployOnBuild=true`: Kích hoạt target đóng gói WPP.
- `/p:WebPublishMethod=FileSystem`: Xuất toàn bộ web ra thư mục hệ thống file phẳng.
- `/p:PublishUrl=...`: Chỉ định chính xác thư mục đầu ra chứa tệp `.aspx`, `Web.config`, và thư mục `bin/`.

### 2.3 Lỗi phân tích cú pháp dấu nháy trên PowerShell Runner
- Trên GitHub Actions `windows-latest` (chạy PowerShell 7 Core), đối số `/p:Platform="Any CPU"` nếu không bọc trong nháy đơn sẽ bị trình phân tích đối số của PowerShell bóc tách thành hai tham số riêng biệt: `/p:Platform=Any` và `CPU`.
- Hậu quả: MSBuild báo lỗi `MSB1008: Only one project can be specified`.
- Khắc phục: Bọc toàn bộ đối số trong nháy đơn: `'/p:Platform="Any CPU"'` hoặc chuyển shell sang `cmd`.

---

## 3. Kiến trúc quản lý gói NuGet trong ASP.NET Web Forms (.NET 4.8.1)
*Nguồn tham chiếu: Microsoft Learn — NuGet Package Restore; packages.config vs PackageReference.*

### 3.1 Dự án dùng `packages.config`
- ASP.NET Web Forms .NET 4.8.1 mặc định sử dụng tệp kê khai `packages.config`.
- Khi thực thi lệnh `nuget restore AspxDemo.sln`:
  - NuGet sẽ tải các gói thư viện và giải nén trực tiếp vào thư mục `.\packages\` nằm cùng cấp với tệp giải pháp `.sln` trong thư mục repo.
  - Các tham chiếu trong `.csproj` trỏ trực tiếp bằng đường dẫn tương đối: `<HintPath>..\packages\Newtonsoft.Json.13.0.3\lib\net45\Newtonsoft.Json.dll</HintPath>`.
- **Hậu quả cấu hình Cache sai trên GitHub Actions**:
  - Nếu workflow cấu hình `path: ~/.nuget/packages` (đây là thư mục cache toàn cục của `PackageReference` trong .NET Core / .NET 8), GitHub Actions sẽ cache một thư mục trống hoặc vô dụng. Khi runner phục hồi cache, thư mục `.\packages` vẫn không tồn tại $\rightarrow$ MSBuild báo lỗi biên dịch thiếu assembly.
  - Giải pháp đúng cho Web Forms:
    ```yaml
    - name: Cache NuGet packages
      uses: actions/cache@v4
      with:
        path: packages
        key: nuget-${{ runner.os }}-${{ hashFiles('**/packages.config') }}
        restore-keys: |
          nuget-${{ runner.os }}-
    ```

### 3.2 Sự cố nâng cấp phụ thuộc với `<bindingRedirect>`
- Khi công cụ như Dependabot nâng cấp một gói NuGet (ví dụ Newtonsoft.Json từ 12.0.1 lên 13.0.3) qua `packages.config`:
  - Dependabot cập nhật file `packages.config` và `.csproj`.
  - Tuy nhiên, trong .NET Framework 4.8.1, mã thực thi nạp assembly dựa vào thẻ `<bindingRedirect>` trong `Web.config`.
  - Nếu không cập nhật `newVersion="13.0.0.0"` trong `Web.config`, IIS runtime sẽ ném ngoại lệ `System.IO.FileLoadException: Could not load file or assembly...`.

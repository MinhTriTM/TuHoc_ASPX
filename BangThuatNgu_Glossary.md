# Bảng thuật ngữ Anh–Việt: Git – GitHub – GitLab (môn ASPX .NET Framework 4.8.1)

> Bảng này chuẩn hóa cách dùng từ trong slide, báo cáo và demo của nhóm 3 thành viên; thuật ngữ kỹ thuật giữ nguyên tiếng Anh khi viết câu lệnh và trao đổi review.

## 1. Nhóm Git (local + cơ chế lõi)

| Thuật ngữ | Nghĩa tiếng Việt | Giải thích 1 dòng |
|---|---|---|
| Repository | Kho chứa mã nguồn | Thư mục có `.git`, lưu toàn bộ lịch sử commit của project ASPX. |
| Working tree | Cây thư mục làm việc | Các file checkout ra đĩa để sửa bằng Visual Studio. |
| Staging area (Index) | Vùng đệm | Nơi gom thay đổi bằng `git add` trước khi commit. |
| Commit | Điểm lưu lịch sử | Một snapshot kèm message, tác giả, thời gian và mã SHA. |
| SHA (hash) | Mã băm định danh | Chuỗi hex định danh duy nhất cho mỗi commit. |
| Blob | Đối tượng file | Object Git lưu nội dung thô của một file. |
| Tree | Đối tượng cây thư mục | Object Git lưu cấu trúc thư mục và danh sách blob. |
| HEAD | Con trỏ HEAD | Con trỏ chỉ commit đang checkout trên nhánh hiện tại. |
| Branch | Nhánh | Dòng phát triển độc lập, ví dụ `main`, `feature/login-aspx`. |
| Default branch (main) | Nhánh chính | Nhánh ổn định để release, luôn được bảo vệ bằng review. |
| Checkout / Switch | Chuyển nhánh | Đổi HEAD sang nhánh khác, ví dụ `git switch develop`. |
| Merge | Hợp nhất | Gộp lịch sử 2 nhánh thành 1, giữ nguyên ngữ cảnh phân nhánh. |
| Merge conflict | Xung đột hợp nhất | Git không tự gộp được, người phải sửa tay rồi commit. |
| Rebase | Dời nền nhánh | Viết lại commit lên đầu nhánh mới để lịch sử thẳng gọn. |
| Cherry-pick | Gắp commit | Sao chép 1 commit lẻ từ nhánh khác sang nhánh hiện tại. |
| Stash | Cất tạm | Lưu tạm thay đổi chưa commit để chuyển nhánh rồi lấy lại. |
| Tag | Thẻ phiên bản | Nhãn cố định cho 1 commit, ví dụ `v1.0-asm`. |
| Reset | Đặt lại | Di chuyển HEAD và nhánh về commit cũ, có 3 mức soft, mixed, hard. |
| Revert | Hoàn tác an toàn | Tạo commit mới đảo ngược commit cũ, dùng cho nhánh public. |
| Reflog | Nhật ký tham chiếu | Lịch sử di chuyển HEAD để cứu commit tưởng đã mất. |
| Remote | Kho từ xa | Bản repo trên server như GitHub hay GitLab, thường tên `origin`. |
| Fetch | Tải về | Tải commit mới từ remote mà chưa gộp vào nhánh local. |
| Pull | Kéo và gộp | Lệnh `fetch` rồi `merge` hoặc rebase trong một bước. |
| Push | Đẩy lên | Gửi commit local lên remote để chia sẻ và review. |

## 2. Nhóm GitHub

| Thuật ngữ | Nghĩa tiếng Việt | Giải thích 1 dòng |
|---|---|---|
| Fork | Bản sao phân nhánh | Sao chép repo sang tài khoản mình để đóng góp độc lập. |
| Pull request (PR) | Yêu cầu kéo | Đề xuất gộp nhánh, kèm diff, thảo luận và review. |
| Code review | Duyệt code | Người khác đọc diff, comment và approve trước khi merge. |
| CODEOWNERS | Chủ sở hữu code | File quy định ai phải review khi chạm vào đường dẫn nào. |
| Protected branch | Nhánh được bảo vệ | Quy tắc cấm push thẳng, bắt buộc PR và check xanh. |
| Ruleset | Bộ quy tắc | Cơ chế GitHub gom nhiều rule bảo vệ nhánh và tag. |
| Issue | Vấn đề | Thẻ việc để báo lỗi, đề xuất tính năng và thảo luận. |
| Project (board) | Bảng quản lý việc | Bảng Kanban gắn issue và PR theo cột Todo, Doing, Done. |
| Wiki | Trang tài liệu | Kho tài liệu Markdown riêng gắn với repo. |
| Gist | Đoạn mã chia sẻ | Dịch vụ chia sẻ snippet nhỏ khi trao đổi ví dụ. |
| GitHub Pages | Trang tĩnh GitHub | Host tài liệu tĩnh từ nhánh `gh-pages` hoặc thư mục docs. |
| Codespaces | Môi trường dev đám mây | VS Code trên trình duyệt kèm container dev dựng sẵn. |
| Copilot | Trợ lý AI | Gợi ý code theo ngữ cảnh khi viết Web Forms và C#. |
| Dependabot | Bot cập nhật phụ thuộc | Tự tạo PR nâng cấp package NuGet có lỗ hổng. |
| CodeQL (code scanning) | Quét mã tĩnh | Phân tích luồng dữ liệu để tìm lỗ hổng bảo mật. |
| Secret scanning | Quét secret lộ | Tự báo khi phát hiện connection string hay token trong commit. |

## 3. Nhóm GitLab

| Thuật ngữ | Nghĩa tiếng Việt | Giải thích 1 dòng |
|---|---|---|
| Group | Nhóm | Đơn vị chứa nhiều project, quản lý member và quyền chung. |
| Project | Dự án | Đơn vị repo trên GitLab gồm code, Issues và CI. |
| Merge request (MR) | Yêu cầu hợp nhất | Khái niệm như PR của GitHub, kèm pipeline và approval. |
| Approval rule | Quy tắc phê duyệt | Quy định số người hay nhóm nào phải approve mới được merge. |
| Merge train | Đoàn tàu hợp nhất | Hàng đợi merge tuần tự kèm pipeline để tránh gãy `main`. |
| Issue board | Bảng issue | Bảng Kanban của GitLab để kéo thả issue theo nhãn. |
| Milestone | Cột mốc | Gom issue và MR phải xong trong 1 đợt nộp bài. |
| Snippet | Đoạn mã | Chia sẻ code mẫu nhỏ trong GitLab, tương tự Gist. |
| Environment | Môi trường triển khai | Đích deploy như staging hay production gắn với pipeline. |
| Review App | App review tạm | Môi trường tự tạo cho mỗi MR để tester mở thử. |
| Container Registry | Kho ảnh container | Nơi lưu Docker image build từ CI của project. |
| Package Registry | Kho gói phần mềm | Nơi lưu package NuGet và npm publish từ pipeline. |
| Self-hosted (self-managed) | Tự vận hành | Mô hình cài GitLab trên server riêng thay vì dùng SaaS. |
| Auto DevOps | DevOps tự động | Pipeline mẫu GitLab tự sinh gồm build, test, scan, deploy. |

## 4. Nhóm CI/CD (dùng chung GitHub Actions và GitLab CI)

| Thuật ngữ | Nghĩa tiếng Việt | Giải thích 1 dòng |
|---|---|---|
| Pipeline | Đường ống CI/CD | Chuỗi stage tự động chạy khi push hoặc mở PR và MR. |
| Stage | Giai đoạn | Nhóm job chạy cùng giai đoạn, ví dụ build rồi mới test. |
| Job | Tác vụ | Đơn vị công việc nhỏ nhất trong pipeline, chạy trên 1 runner. |
| Runner | Máy chạy CI | Máy thực thi job, project 4.8.1 cần Windows runner. |
| Workflow | Quy trình công việc | File YAML định nghĩa pipeline trong GitHub Actions. |
| Artifact | Hiện vật build | File kết quả job giữ lại, ví dụ gói publish Web Forms. |
| Cache | Bộ nhớ đệm | Lưu thư mục NuGet `packages` để lần build sau nhanh hơn. |
| Secret | Bí mật | Biến nhạy cảm đã mã hóa như connection string, token deploy. |
| Environment variable | Biến môi trường | Biến cấu hình truyền vào job, ví dụ `Configuration=Release`. |
| Trigger | Điều kiện kích hoạt | Sự kiện chạy pipeline như push, PR, hẹn giờ hoặc gọi tay. |
| Status check | Kiểm tra trạng thái | Kết quả job bắt buộc xanh mới cho merge PR và MR. |
| Deployment | Triển khai | Đưa gói publish ASPX lên IIS ở staging hoặc production. |
| Rollback | Quay lui bản triển khai | Đưa môi trường về artifact ổn định trước đó khi lỗi. |
| Badge | Huy hiệu trạng thái | Ảnh nhỏ hiển thị passing hay failing của pipeline trong README. |
| Protected environment | Môi trường bảo vệ | Môi trường yêu cầu approve tay trước khi deploy. |
| MSBuild | Công cụ build .NET | Trình build chính cho solution ASPX 4.8.1 trên Windows. |

## Ghi chú áp dụng cho project ASPX 4.8.1

- Build project ASPX 4.8.1 dùng `msbuild` trên Windows runner, không dùng `dotnet build` trên Ubuntu.
- Không commit connection string thật; lưu vào Secret của Actions hay GitLab CI và đọc qua biến môi trường.
- Mọi thay đổi vào `main` đi qua Pull Request hay Merge Request với ít nhất 1 approve và pipeline xanh.

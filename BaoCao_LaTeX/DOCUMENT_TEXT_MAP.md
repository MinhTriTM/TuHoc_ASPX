# Document Text & Page Navigation Map

> [!IMPORTANT]
> Text navigation index. For proofs and figures, inspect page images in `page_image_dir`.

## [Page 1] (`page-1.png`)

TRƯỜNG ĐẠI HỌC
KHOA CÔNG NGHỆ THÔNG TIN
BÁO CÁO BÀI TRÌNH BÀY
Đề tài: GIT – GitHub – GitLab
Học phần ASPX (.NET Framework 4.8.1)
Nhóm 3 thành viên
TV1 – MSSV1
TV2 – MSSV2
TV3 – MSSV3
Ngày Ngày 15 tháng 11 năm 2026

---

## [Page 2] (`page-2.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Mục lục
Mục lục 1
1 Giới thiệu 5
1.1 Lý do chọn đề tài . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.1.1 Kịch bản mất bài điển hình trong một tuần . . . . . . . . . . . . . 6
1.2 Mục tiêu đề tài . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
1.3 Phạm vi và đối tượng . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.3.1 Đối tượng áp dụng . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.3.2 Phạm vi nội dung . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.4 Liên hệ với học phần ASPX . . . . . . . . . . . . . . . . . . . . . . . . . . 9
1.4.1 Mô hình Web Forms và code-behind . . . . . . . . . . . . . . . . . 9
1.4.2 File Web.config và quy trình biên dịch . . . . . . . . . . . . . . . . 9
1.5 Phương pháp thực hiện . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
1.6 Cấu trúc báo cáo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2 Git căn bản 13
2.1 Lịch sử Git và mô hình phân tán . . . . . . . . . . . . . . . . . . . . . . . 14
2.2 Kiến trúc 3 vùng và thư mục .git . . . . . . . . . . . . . . . . . . . . . . . 15
2.3 Cài đặt và cấu hình đầu tiên . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.3.1 Mức cấu hình và danh sách kiểm tra sau cài đặt . . . . . . . . . . . 19
2.3.2 Commit đầu tiên cho project ASPX mẫu . . . . . . . . . . . . . . . 20
2.3.3 Ghi nhớ credential và ba lỗi cấu hình phổ biến . . . . . . . . . . . . 20
2.4 Vòng đời file và commit đầu tiên . . . . . . . . . . . . . . . . . . . . . . . 21
2.5 Xem lịch sử và so sánh . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
2.6 Hoàn tác thay đổi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
2.7 Stash và tag . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
2.8 Nhánh trong Git: con trỏ nhẹ và thao tác cơ bản . . . . . . . . . . . . . . 27
2.9 Hợp nhất nhánh và giải quyết xung đột . . . . . . . . . . . . . . . . . . . . 29
2.10 Tệp .gitignore chuẩn cho dự án ASP.NET . . . . . . . . . . . . . . . . . . 31
2.11 Dự án mini với ASPX: tạo trang, commit và xem lịch sử . . . . . . . . . . 32
3 Git nâng cao và chuyên sâu 35
3.1 Mô hình đối tượng: blob, tree, commit và tag . . . . . . . . . . . . . . . . 35
3.2 Đồ thị DAG, refs và HEAD . . . . . . . . . . . . . . . . . . . . . . . . . . 37
3.3 Reflog và khôi phục commit tưởng chừng đã mất . . . . . . . . . . . . . . 38
3.4 Packfile và bảo trì kho . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
3.5 Rebase và rebase tương tác . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
3.6 So sánh merge, rebase và cherry-pick . . . . . . . . . . . . . . . . . . . . . 42
1

---

## [Page 3] (`page-3.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
3.7 Cherry-pick và bản vá nóng . . . . . . . . . . . . . . . . . . . . . . . . . . 43
3.8 Git bisect truy tìm commit gây lỗi . . . . . . . . . . . . . . . . . . . . . . 44
3.9 Rerere và worktree . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
3.9.1 Cơ chế ghi nhớ cách giải conflict của rerere . . . . . . . . . . . . . . 46
3.9.2 Làm nhiều nhánh cùng lúc với worktree . . . . . . . . . . . . . . . 46
3.10 Git hooks: kiểm soát tự động với pre-commit, commit-msg và pre-push . . 47
3.11 Git LFS: quản lý file lớn như video, bộ cài đặt và thư viện dll . . . . . . . 48
3.12 Submodule và subtree: tái sử dụng mã nguồn giữa các repo . . . . . . . . . 49
3.13 Ký commit bằng GPG và SSH: chống giả mạo tác giả . . . . . . . . . . . . 50
3.14 Sparse-checkout và partial clone cho repo khổng lồ . . . . . . . . . . . . . . 50
3.15 Viết lại lịch sử an toàn với filter-repo khi lộ connection string . . . . . . . 51
3.16 Quy trình nhánh: GitFlow, GitHub Flow và Trunk-Based Development . . 52
3.17 Conventional Commits: chuẩn hóa thông điệp commit cho cả nhóm . . . . 53
4 GitHub 54
4.1 Tổng quan: Git là công cụ, GitHub là nền tảng cộng tác . . . . . . . . . . 54
4.2 Kho chứa, Issues, Projects, Wiki và Discussions . . . . . . . . . . . . . . . 55
4.3 Fork và Pull Request . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
4.4 Đánh giá code: approve, request changes và suggest . . . . . . . . . . . . . 58
4.5 Bảo vệ nhánh và CODEOWNERS . . . . . . . . . . . . . . . . . . . . . . 59
4.6 Khái niệm: workflow, job, step, runner và trigger . . . . . . . . . . . . . . 61
4.7 Workflow CI đầy đủ cho ASPX 4.8.1 . . . . . . . . . . . . . . . . . . . . . 62
4.7.1 Tệp workflow hoàn chỉnh . . . . . . . . . . . . . . . . . . . . . . . . 62
4.7.2 Giải thích từng bước . . . . . . . . . . . . . . . . . . . . . . . . . . 64
4.8 Secrets và Environments . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
4.9 Cache NuGet và artifacts . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
4.10 Runner Windows và Ubuntu cho .NET Framework 4.8.1 . . . . . . . . . . 67
4.11 Packages và Pages: gói NuGet nội bộ và trang tài liệu . . . . . . . . . . . . 68
4.12 Codespaces: môi trường phát triển trên mây . . . . . . . . . . . . . . . . . 70
4.13 Copilot: trợ lý gợi ý code bằng AI . . . . . . . . . . . . . . . . . . . . . . . 71
4.14 Bảo mật nâng cao: quét secret, Dependabot và CodeQL . . . . . . . . . . . 72
4.15 Gói GitHub Education cho sinh viên . . . . . . . . . . . . . . . . . . . . . 74
5 GitLab 74
5.1 Tổng quan GitLab: nền tảng DevOps tích hợp . . . . . . . . . . . . . . . . 75
5.2 Groups, Projects, Issues, Boards, Milestones, Wiki, Snippets . . . . . . . . 76
5.3 Merge Request và Approval rules . . . . . . . . . . . . . . . . . . . . . . . 78
5.4 Bảo vệ nhánh và tag . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
5.5 Khái niệm pipeline: stages, jobs, artifacts, cache, needs và rules . . . . . . 80
5.6 Tệp cấu hình hoàn chỉnh cho dự án ASPX 4.8.1 . . . . . . . . . . . . . . . 81
2

---

## [Page 4] (`page-4.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
5.7 Runner: shared, specific, group và vai trò của tag . . . . . . . . . . . . . . 83
5.8 Biến CI/CD: masked, protected và cách đọc qua biến môi trường . . . . . 85
5.9 Môi trường triển khai và Review Apps . . . . . . . . . . . . . . . . . . . . 86
5.10 Container Registry và Package Registry lưu trữ nội bộ . . . . . . . . . . . 87
5.11 Merge trains gộp nhiều Merge Request song song an toàn . . . . . . . . . . 88
5.12 Quét bảo mật tích hợp trong pipeline . . . . . . . . . . . . . . . . . . . . . 89
5.13 Kiểm toán và tuân thủ với Audit Events . . . . . . . . . . . . . . . . . . . 91
5.14 Tự host GitLab và sao lưu phục hồi . . . . . . . . . . . . . . . . . . . . . . 91
5.15 Auto DevOps pipeline tự sinh cho dự án mới . . . . . . . . . . . . . . . . . 92
5.16 Các gói Free, Premium, Ultimate và gợi ý cho đồ án môn học . . . . . . . 93
6 So sánh Git, GitHub và GitLab 94
6.1 Git, GitHub và GitLab khác nhau thế nào . . . . . . . . . . . . . . . . . . 94
6.2 So sánh chi tiết GitHub và GitLab trên hơn hai mươi tiêu chí . . . . . . . 96
6.3 Các tính năng tương đương giữa hai nền tảng . . . . . . . . . . . . . . . . 98
6.4 Khuyến nghị cho đồ án môn học ASPX . . . . . . . . . . . . . . . . . . . . 100
6.4.1 Khi nào nên chọn GitHub . . . . . . . . . . . . . . . . . . . . . . . 100
6.4.2 Khi nào nên chọn GitLab . . . . . . . . . . . . . . . . . . . . . . . 100
6.4.3 Vì sao nhóm dùng cả hai qua cơ chế mirror . . . . . . . . . . . . . 100
7 Áp dụng vào học phần ASPX 102
7.1 Tổ chức nhóm 3 người và mô hình nhánh . . . . . . . . . . . . . . . . . . . 102
7.2 Quy trình pull request và merge request sáu bước . . . . . . . . . . . . . . 103
7.3 Danh sách kiểm tra review code Web Forms . . . . . . . . . . . . . . . . . 104
7.4 Xử lý xung đột file Web.config . . . . . . . . . . . . . . . . . . . . . . . . . 105
7.5 Quản lý connection string và secret . . . . . . . . . . . . . . . . . . . . . . 106
7.6 Mẫu lịch sử commit và quy tắc đặt message . . . . . . . . . . . . . . . . . 107
7.7 Bài tập thực hành . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
8 Kết luận 109
8.1 Tổng kết: đối chiếu mục tiêu và kết quả . . . . . . . . . . . . . . . . . . . . 109
8.2 Hạn chế . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
8.3 Hướng phát triển . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
A Bảng lệnh Git tra cứu nhanh 113
A.1 Nhóm Khởi tạo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
A.2 Nhóm Commit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
A.3 Nhóm Lịch sử . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
A.4 Nhóm Nhánh . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
A.5 Nhóm Merge/Rebase . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
3

---

## [Page 5] (`page-5.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
A.6 Nhóm Hoàn tác . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
A.7 Nhóm Stash/Tag . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
A.8 Nhóm Remote . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
A.9 Nhóm Nâng cao . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
B Tệp gitignore mẫu cho ASP.NET 118
B.1 Nội dung mẫu . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
B.2 Giải thích từng khối . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
B.3 Đã commit nhầm thì sửa sao . . . . . . . . . . . . . . . . . . . . . . . . . . 122
C Mẫu CI/CD hoàn chỉnh 124
C.1 GitHub Actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
C.2 GitLab CI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
C.3 Tham số MSBuild hay dùng . . . . . . . . . . . . . . . . . . . . . . . . . . 129
D Kịch bản demo trên lớp 130
D.1 Demo TV1: Git local . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
D.2 Demo TV2: GitHub . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
D.3 Demo TV3: GitLab . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
D.4 Dự phòng sự cố . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
Tài liệu 138
4

---

## [Page 6] (`page-6.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
1 Giới thiệu
Đồ án môn ASPX được thực hiện theo nhóm ba sinh viên trên cùng một project ASP.NET
Web Forms chạy trên .NET Framework 4.8.1. Mỗi thành viên cùng chỉnh sửa các file giao
diện Default.aspx, file code-behind Default.aspx.cs và file cấu hình Web.config trong
cùng một thư mục project. Khi ba người cùng sửa chung một bộ file mà không có công
cụ quản lý phiên bản, nhóm rất dễ rơi vào tình trạng đè code của nhau, mất bài đã làm
hoặc nộp thiếu file vào phút cuối. Đề tài GIT — GitHub — GitLab của nhóm ra đời
từ chính nhu cầu thực tế đó: xây dựng một quy trình làm việc nhóm có kỷ luật, minh
bạch và kiểm chứng được cho đồ án ASPX. Báo cáo này trình bày toàn bộ hành trình từ
Git căn bản trên máy cá nhân, Git nâng cao, GitHub, GitLab cho đến pipeline CI/CD
biên dịch thật project ASPX 4.8.1 và quy trình phối hợp của cả nhóm. Mọi lý thuyết đều
đi kèm lệnh chạy được, hình minh họa và ví dụ gắn với project demo Web Forms để người
đọc có thể làm theo từng bước và kiểm tra kết quả ngay.
1.1 Lý do chọn đề tài
Khi làm đồ án ASPX theo nhóm, cách làm phổ biến của sinh viên là nén cả thư mục
project rồi gửi qua tin nhắn hoặc USB cho nhau. Cách làm này bộc lộ rất nhiều vấn
đề ngay từ tuần đầu tiên, đặc biệt khi ba người cùng sửa các file .aspx, .aspx.cs và
Web.config. Nhóm đã tổng hợp các nỗi đau điển hình nhất mà hầu như nhóm ASPX
nào cũng từng gặp qua như sau.
• Đè code và mất bài: hai thành viên cùng sửa một trang, bản nộp cuối cùng chỉ
giữ lại thay đổi của một người, công sức của người còn lại biến mất mà không để
lại bất kỳ dấu vết nào.
• Không truy vết được ai đã sửa gì: khi trang web bỗng nhiên báo lỗi, nhóm
không thể trả lời câu hỏi ai đã đổi dòng nào, đổi lúc nào và đổi vì lý do gì.
• Xung đột file Web.config: đây là file dùng chung chứa chuỗi kết nối cơ sở dữ liệu
và cấu hình ứng dụng, nên hầu như mọi nhánh công việc đều chạm vào nó và gây
xung đột mỗi lần gộp code.
• Rò rỉ thông tin nhạy cảm: chuỗi kết nối chứa mật khẩu thật bị gửi kèm trong
file nén qua kênh chat chung, ai cũng đọc được và nhóm không có cách nào thu hồi.
• Không quay lui được: sau khi sửa hỏng một form phức tạp, nhóm không có bản
tốt gần nhất để quay về nên đành mất hàng giờ viết lại từ đầu.
• Nộp bài thiếu file: lúc nén project, người nộp quên kèm thư mục bin, quên file
cấu hình hoặc nộp nhầm bản cũ, khiến bài chạy trên máy của thầy cô khác hẳn
5

---

## [Page 7] (`page-7.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
máy của nhóm.1
Git giải quyết triệt để các vấn đề trên vì mọi thay đổi đều được ghi lại thành lịch sử
có tác giả, thời điểm và lý do kèm theo [1]. Mỗi thành viên làm việc trên một nhánh riêng
rồi gộp lại có kiểm soát, xung đột được phát hiện sớm và xử lý ngay thay vì dồn đến sát
ngày nộp bài. GitHub và GitLab tiếp tục mở rộng Git từ máy cá nhân lên môi trường
cộng tác trực tuyến với pull request, review code và pipeline tự động [6, 8]. Với project
ASPX 4.8.1, pipeline còn tự động biên dịch bằng msbuild sau mỗi lần đẩy code, giúp
nhóm phát hiện lỗi vỡ build chỉ sau vài phút thay vì đến lúc nộp mới biết. Vì vậy nhóm
chọn đề tài này với kỳ vọng kép: vừa học vững công cụ dùng cho mọi đồ án sau này, vừa
xây dựng ngay một quy trình mẫu áp dụng được cho chính đồ án ASPX của nhóm. Điểm
khởi đầu rất đơn giản: chỉ cần khởi tạo kho chứa và tạo commit đầu tiên như ví dụ dưới
đây là nhóm đã có lịch sử để đối chiếu mỗi khi có sự cố.
1 # Kiem tra Git va cau hinh danh tinh ( chi lam mot lan )
2 git -- version
3 git config -- global user . name " Nguyen Van A "
4 git config -- global user . email " nva@student . edu . vn "
5 # Tao thu muc project demo ASPX va tao commit dau tien
6 mkdir AspxDemo - NET481
7 cd AspxDemo - NET481
8 git init
9 git add .
10 git commit -m " docs : khoi tao repo demo ASPX 4.8.1 "
11 git log -- oneline
12 git status
Từ commit đầu tiên này, mọi lần sửa trang .aspx hay file Web.config đều để lại vết
trong lịch sử và nhóm không bao giờ còn cảnh mất bài không rõ nguyên nhân. Chương
2 sẽ hệ thống hóa toàn bộ thao tác Git hằng ngày mà thành viên nào trong nhóm cũng
phải thành thạo.
1.1.1 Kịch bản mất bài điển hình trong một tuần
Để thấy rõ nỗi đau, nhóm kể lại một tuần làm việc có thật của chính nhóm trước khi áp
dụng Git, với ba thành viên cùng sửa trang quản lý sinh viên. Sáng thứ hai, TV1 nén cả
project gửi vào nhóm chat và dặn mọi người lấy đó làm “bản gốc” để bắt đầu tuần mới.
Chiều thứ ba, TV2 sửa giao diện Student.aspx cho đẹp hơn rồi nén gửi lại, trong khi
TV1 vẫn đang viết dở hàm lưu dữ liệu trên bản cũ tải từ hôm thứ hai. Sáng thứ tư, TV3
sửa Web.config để trỏ sang máy chủ mới rồi gửi bản của mình lên, lúc này trong nhóm
1Thực tế nhiều nhóm còn nộp kèm cả thư mục packages nặng hàng trăm MB trong khi lại thiếu đúng
file quan trọng nhất.
6

---

## [Page 8] (`page-8.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
chat đã có ba bản nén khác nhau mà không ai biết bản nào mới nhất. Tối thứ năm, TV1
gộp bằng tay: chép đè file .aspx của TV2 vào bản của mình, chép đè Web.config của
TV3, rồi chạy thử và thấy trang báo lỗi vì hàm code-behind không khớp với giao diện
mới. Cả ba thức đến nửa đêm để dò từng dòng, cuối cùng phát hiện TV2 đã đổi tên nút
bấm mà TV1 không hề biết, còn chuỗi kết nối của TV3 lại trỏ về máy chủ cũ trên máy
TV1. Sáng thứ sáu nộp bài, nhóm nộp vội bản chạy được trên máy TV1 nhưng thiếu
form thống kê mà TV2 đã làm xong từ thứ tư, đơn giản vì file đó nằm trong bản nén bị
bỏ quên. Hậu quả không chỉ là mất điểm bài nộp mà còn là mâu thuẫn nội bộ, vì không
ai chứng minh được phần việc của mình đã hoàn thành đúng hạn. TV2 ấm ức vì form
thống kê tâm huyết bị loại khỏi bản nộp, TV1 mệt mỏi vì phải gộp tay trong đêm, còn
TV3 lo lắng vì mật khẩu máy chủ nằm trong file nén gửi công khai. Câu chuyện trên
không phải cá biệt: bất kỳ nhóm nào cộng tác bằng file nén đều có nguy cơ lặp lại đúng
kịch bản này mỗi tuần. Từ tuần lễ mất bài đó, nhóm rút ra năm bài học xương máu làm
kim chỉ nam cho toàn bộ đề tài.
• Mọi thay đổi phải có tác giả và thời điểm, nếu không nhóm sẽ tranh cãi bất tận
mỗi khi có lỗi mà chẳng ai chịu trách nhiệm.
• Mỗi người phải làm trên nhánh riêng, nếu không bản nộp cuối cùng chỉ là bản của
người gửi file muộn nhất chứ không phải bản tốt nhất.
• File dùng chung như Web.config phải có chủ sở hữu và quy trình sửa đổi riêng,
nếu không xung đột sẽ nổ ra ngay trước giờ nộp bài.
• Mật khẩu và chuỗi kết nối không bao giờ được gửi qua kênh chat chung, nếu không
nhóm vừa mất an toàn vừa không thể thu hồi khi lộ.
• Bản nộp phải được lấy từ một nguồn duy nhất đã qua kiểm tra tự động, nếu không
nhóm sẽ nộp thiếu file hoặc nộp nhầm bản cũ như cơm bữa.
Git cùng GitHub và GitLab đáp ứng cả năm bài học trên: ghi lại mọi thay đổi, tách mỗi
người một nhánh, gộp có kiểm soát kèm review và biên dịch tự động trước khi cho phép
gộp. Sau khi áp dụng Git, tuần làm việc của nhóm thay đổi hẳn: xung đột hiện ra ngay
lúc gộp nhánh, ai sửa gì đều có tên trong lịch sử và bản nộp luôn được lấy từ nhánh main
đã qua pipeline. Thành viên mới chỉ cần đọc lịch sử commit là nắm được tiến độ nhóm,
thay vì phải hỏi từng người xem bản mới nhất đang nằm ở đâu. Bảng phân công trong
Bảng 1 ở cuối chương cũng được rút ra từ chính bài học phân việc rõ ràng này.
1.2 Mục tiêu đề tài
Đề tài đặt ra sáu mục tiêu cụ thể, mỗi mục tiêu tương ứng với một khối kiến thức mà
nhóm phải làm chủ và chứng minh bằng sản phẩm chạy được. Sáu mục tiêu này cũng
chính là sáu mảng nội dung của các chương tiếp theo trong báo cáo.
7

---

## [Page 9] (`page-9.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
• Nắm vững Git căn bản: thành thạo khoảng hai mươi lệnh dùng hằng ngày gồm
khởi tạo kho chứa, ghi nhận thay đổi, xem lịch sử, làm việc với nhánh, gộp nhánh
và hoàn tác an toàn trên project ASPX demo.
• Làm chủ Git nâng cao: hiểu cấu trúc trong của Git gồm blob, tree và commit,
đồng thời sử dụng được rebase tương tác, cherry-pick, stash, reflog, tag, hook và
quy ước Conventional Commits cho lịch sử sạch đẹp.
• Khai thác GitHub cho cộng tác: dùng thành thạo issue, fork, pull request,
review code, nhánh được bảo vệ và quy tắc review, mọi thay đổi đều đi qua pull
request có ít nhất một người duyệt trước khi gộp [6].
• Khai thác GitLab cho cộng tác: dùng thành thạo group, project, merge request,
quy tắc phê duyệt và môi trường triển khai, đồng thời so sánh được điểm giống và
khác với GitHub trên cùng một repo demo [8].
• Xây dựng CI/CD thật cho ASPX 4.8.1: dựng pipeline biên dịch tự động bằng
msbuild trên cả GitHub Actions và GitLab CI với Windows runner, pipeline phải
chạy xanh và báo lỗi vỡ build cho nhóm sau mỗi lần đẩy code [5, 7].
• Thiết lập quy trình nhóm ba người: ban hành quy trình nhánh main, develop
và feature, checklist review cho Web Forms, cách xử lý xung đột Web.config và
cách quản lý chuỗi kết nối an toàn bằng secret của pipeline.
Hoàn thành sáu mục tiêu trên, nhóm có trong tay cả kiến thức, repo demo có lịch sử mẫu
và hai pipeline chạy xanh để minh chứng trong buổi thuyết trình.
1.3 Phạm vi và đối tượng
1.3.1 Đối tượng áp dụng
Đối tượng chính của báo cáo là sinh viên đang học học phần ASPX và phải làm đồ án
Web Forms theo nhóm từ hai đến bốn người. Người đọc được giả định đã biết lập trình
C# ở mức cơ bản và đã tạo được một project Web Forms đơn giản trong Visual Studio.
Người đọc chưa cần biết Git từ trước vì báo cáo đi từ con số không: cài đặt, cấu hình
danh tính rồi mới đến từng lệnh đầu tiên. Giảng viên và các nhóm khóa sau cũng có thể
dùng báo cáo như một giáo trình thực hành vì mọi ví dụ đều chạy được và gắn với project
ASPX 4.8.1 cụ thể.
1.3.2 Phạm vi nội dung
Về nội dung, báo cáo bao phủ toàn bộ vòng đời cộng tác trên một repo demo ASPX duy
nhất là AspxDemo-NET481. Các mảng nằm trong phạm vi gồm có:
8

---

## [Page 10] (`page-10.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
• Git cục bộ từ căn bản đến nâng cao, thao tác trực tiếp trên các file .aspx, .aspx.cs
và Web.config của project demo.
• GitHub và GitLab ở mức cộng tác nhóm nhỏ: issue, pull request và merge request,
review, nhánh được bảo vệ và quản lý secret.
• Pipeline CI/CD biên dịch project .NET Framework 4.8.1 bằng msbuild trên Win￾dows runner của cả hai nền tảng.
• Quy trình làm việc nhóm ba người, checklist review, xử lý xung đột và bài tập thực
hành có rubric chấm điểm.
Ngược lại, các nội dung sau nằm ngoài phạm vi để báo cáo giữ được độ sâu cần thiết:
• Các framework mới như ASP.NET Core, MVC hay Blazor vì học phần chỉ yêu cầu
Web Forms trên .NET Framework 4.8.1.
• Quản trị hạ tầng như dựng server GitLab self-hosted, cấu hình Kubernetes hay triển
khai production thực tế cho doanh nghiệp.
• Các chủ đề Git rất chuyên sâu về vận hành như viết Git server riêng hay tối ưu kho
chứa hàng chục GB mã nguồn.
1.4 Liên hệ với học phần ASPX
1.4.1 Mô hình Web Forms và code-behind
Học phần ASPX giảng dạy ASP.NET Web Forms, mô hình lập trình web theo hướng sự
kiện trong đó mỗi trang gồm hai file đi thành cặp [10]. File .aspx chứa đánh dấu giao
diện gồm các control như TextBox, Button và GridView cùng bố cục HTML của trang.
File .aspx.cs là code-behind viết bằng C#, chứa các hàm xử lý sự kiện như nhấn nút
hay tải trang, gắn với giao diện qua cơ chế partial class. Chính vì giao diện và logic tách
thành hai file nhưng luôn phải sửa đồng bộ nên khi hai người cùng sửa một trang mà
không có Git, nhóm rất dễ gộp sót một trong hai file. Git giúp mỗi cặp file giao diện và
code-behind luôn được commit cùng nhau thành một đơn vị thay đổi hoàn chỉnh, xem lại
lịch sử là thấy rõ mỗi tính năng đã đổi những trang nào.
1.4.2 File Web.config và quy trình biên dịch
File Web.config là file cấu hình dạng XML của ứng dụng, chứa chuỗi kết nối trong thẻ
connectionStrings, tham số ứng dụng trong thẻ appSettings và các thiết lập biên dịch
[10]. Đây là file nhạy cảm nhất trong project vì vừa dùng chung cho cả nhóm, vừa chứa
mật khẩu cơ sở dữ liệu, vừa khác nhau giữa máy lập trình và máy chấm bài. Project
ASPX 4.8.1 được biên dịch bằng msbuild trên Windows thay vì lệnh dotnet build đa
9

---

## [Page 11] (`page-11.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
nền tảng, vì .NET Framework gắn chặt với hệ điều hành Windows [9]. Hiểu rõ đặc điểm
này giúp nhóm cấu hình pipeline đúng ngay từ đầu: dùng Windows runner, khôi phục gói
NuGet rồi mới gọi msbuild với đúng configuration và platform. Tóm lại, kiến thức Git
trong báo cáo không đứng riêng lẻ mà luôn được đặt cạnh ba khái niệm cốt lõi của học
phần là trang .aspx, code-behind .aspx.cs và file Web.config.
1.5 Phương pháp thực hiện
Nhóm thực hiện đề tài theo phương pháp học đi đôi với làm thật trên repo demo, mỗi lý
thuyết học được đều phải kiểm chứng bằng lệnh chạy được. Quy trình gồm năm bước lặp
lại cho từng chương, do cả ba thành viên cùng tham gia và review chéo cho nhau.
1. Học tài liệu gốc: đọc sách Pro Git cho nền tảng Git [2], đọc tài liệu chính thức
của GitHub và GitLab cho phần cộng tác [6, 8], đọc tài liệu Microsoft cho phần
Web Forms và MSBuild [10, 9].
2. Dựng repo demo dùng chung: tạo project AspxDemo-NET481 đúng chuẩn Web
Forms 4.8.1, viết file .gitignore chuẩn cho ASP.NET rồi tạo lịch sử commit mẫu
để mọi ví dụ trong báo cáo đều có chỗ kiểm chứng.
3. Mỗi người một nhánh feature: ba thành viên thực hành song song trên ba nhánh
riêng, mọi thay đổi đều đi qua pull request hoặc merge request có review, tuyệt đối
không đẩy thẳng lên nhánh main.
4. Dựng pipeline chạy thật: viết file ci-aspx-481.yml cho GitHub Actions và file
.gitlab-ci.yml cho GitLab CI, cả hai đều biên dịch bằng msbuild trên Windows
runner và phải đạt trạng thái xanh trước khi viết báo cáo.
5. Tổng hợp và review chéo: mỗi chương do một thành viên viết nháp, hai thành
viên còn lại review qua pull request, mọi lệnh trong báo cáo đều được chạy lại từ
đầu để bảo đảm độc giả làm theo là thành công.
Ví dụ dưới đây mô tả vòng đời chuẩn của một tính năng nhỏ trong repo demo, từ lúc tạo
nhánh đến lúc đẩy lên để xin review.
1 # Tai repo demo ve may va tao nhanh chuc nang rieng
2 git clone https :// github . com / nhom3 / AspxDemo - NET481 . git
3 cd AspxDemo - NET481
4 git checkout -b feature / sua - trang - login
5 # Sua file Default . aspx roi ghi nhan thay doi
6 git status
7 git add Default . aspx Default . aspx . cs
8 git commit -m " feat : them o nhap email o trang dang nhap "
9 git push -u origin feature / sua - trang - login
10

---

## [Page 12] (`page-12.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
10 git log -- oneline -5
Nhờ tuân thủ vòng đời này cho cả báo cáo lẫn code, nhóm vừa có sản phẩm demo thuyết
phục, vừa tự mình trải nghiệm đúng quy trình mà báo cáo khuyến nghị. Kinh nghiệm va
vấp thực tế như xung đột Web.config hay pipeline báo đỏ đều được ghi lại thành bài học
trong Chương 7.
Ngoài năm bước trên, nhóm còn áp dụng ba kỷ luật bắt buộc cho mọi thành viên trong
suốt quá trình thực hiện đề tài. Thứ nhất, mọi commit đều tuân theo quy ước Conventional
Commits với tiền tố nói rõ loại thay đổi ngay từ đầu dòng [3]. Tiền tố feat: dùng cho tính
năng mới như thêm trang đăng nhập, fix: dùng cho sửa lỗi như sửa xung đột Web.config,
còn docs: dùng cho báo cáo và slide. Ví dụ docs: bo sung muc tieu de tai chuong 1
cho người đọc biết ngay đây là commit tài liệu mà không cần mở nội dung ra xem. Thứ
hai, không ai được đẩy thẳng lên nhánh main, mọi thay đổi đều phải đi qua pull request
hoặc merge request có ít nhất một người review. Thứ ba, pull request chỉ được gộp khi
pipeline báo xanh, tức là project ASPX 4.8.1 đã biên dịch thành công bằng msbuild trên
Windows runner. Ba kỷ luật này tuy đơn giản nhưng tạo ra khác biệt lớn: lịch sử commit
sạch đẹp và mọi ví dụ trong báo cáo đều đã có ít nhất hai người kiểm chứng độc lập. Đi
kèm ba kỷ luật là checklist review mà mọi pull request chạm vào Web Forms đều phải
vượt qua trước khi gộp.
• Cặp file .aspx và .aspx.cs luôn được sửa đồng bộ, đổi tên control ở giao diện thì
phải sửa hàm bắt sự kiện tương ứng.
• File Web.config không chứa mật khẩu thật, chuỗi kết nối của máy lập trình được
thay bằng giá trị mẫu trước khi commit.
• Mọi tính năng mới đều có ảnh chụp trang chạy được đính kèm trong phần mô tả
của pull request để người review đối chiếu.
• Pipeline biên dịch báo xanh và không có cảnh báo mới so với nhánh main, nếu
pipeline báo đỏ thì review dừng lại ngay.
Nhóm cũng ghi nhật ký thực nghiệm sau mỗi buổi làm việc, ghi lại lệnh đã chạy, lỗi đã
gặp và cách khắc phục để đưa vào Chương 7 và phụ lục. Cách làm này bảo đảm báo cáo
cuối cùng phản ánh đúng thực tế đã kiểm chứng chứ không phải lý thuyết chép lại từ tài
liệu.
1.6 Cấu trúc báo cáo
Ngoài chương mở đầu này, báo cáo gồm bảy chương chính và một cụm phụ lục, đi từ Git
cục bộ đến cộng tác trực tuyến rồi kết thúc bằng quy trình nhóm. Bạn đọc nên đọc tuần
tự từ Chương 2 đến Chương 5 để nắm công cụ, sau đó đọc Chương 6 và Chương 7 để biết
cách chọn công cụ và phối hợp nhóm. Nội dung tóm tắt từng chương như sau.
11

---

## [Page 13] (`page-13.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
• Chương 1. Giới thiệu: lý do chọn đề tài, sáu mục tiêu, phạm vi và đối tượng, liên
hệ với học phần ASPX, phương pháp thực hiện và cấu trúc toàn báo cáo.
• Chương 2. Git căn bản: lịch sử Git, kiến trúc ba vùng và thư mục .git, cài đặt
và cấu hình, các lệnh hằng ngày, nhánh và gộp nhánh, hoàn tác, stash, tag và file
.gitignore cho ASP.NET.
• Chương 3. Git nâng cao: cấu trúc trong gồm blob, tree và commit, rebase tương
tác, cherry-pick, reflog, hook, Git LFS, submodule, worktree, ký commit và các mô
hình nhánh như GitFlow.
• Chương 4. GitHub: tổng quan nền tảng, issue và project, fork và pull request,
nhánh được bảo vệ, GitHub Actions biên dịch ASPX 4.8.1, packages, bảo mật nâng
cao và Copilot.
• Chương 5. GitLab: group và project, issue và board, merge request và quy tắc
phê duyệt, CI/CD với Windows runner, môi trường triển khai, registry và so sánh
bản self-hosted với bản SaaS.
• Chương 6. So sánh: bảng so sánh hơn hai mươi tiêu chí giữa Git với GitHub và
GitLab, cùng bảng đối đầu trực tiếp GitHub với GitLab về giá, CI/CD, review, bảo
mật và độ phù hợp với đồ án ASPX.
• Chương 7. Áp dụng nhóm: quy trình ba người với main, develop và feature,
checklist review Web Forms, xử lý xung đột Web.config, quản lý secret, lịch sử
commit mẫu và bài tập có rubric.
• Chương 8. Kết luận: tổng kết kết quả đạt được so với sáu mục tiêu, nêu hạn chế
của đề tài và đề xuất hướng phát triển cho các nhóm khóa sau.
• Phụ lục: bảng tra cứu lệnh Git, file .gitignore mẫu, file YAML mẫu cho hai
pipeline, kịch bản demo buổi thuyết trình và bảng phân công chi tiết.
Bảng phân công chi tiết từng chương cho ba thành viên được trình bày trong Bảng 1.
12

---

## [Page 14] (`page-14.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Bảng 1: Bảng phân công các chương báo cáo cho ba thành viên
Chương Nội dung chính Phụ trách
Chương 1 Giới thiệu: lý do, mục tiêu, phạm vi, phương
pháp
TV1
Chương 2 Git căn bản và demo trên project ASPX TV1
Chương 3 Git nâng cao và mô hình nhánh TV1
Chương 4 GitHub và pipeline GitHub Actions TV2
Chương 5 GitLab và pipeline GitLab CI TV3
Chương 6 So sánh Git với GitHub và GitLab TV3
Chương 7 Quy trình nhóm ba người và bài tập TV3
Chương 8 Kết luận và hướng phát triển TV3
Phụ lục Bảng lệnh, file mẫu, kịch bản demo Cả nhóm
Lộ trình đọc khuyến nghị được minh họa trong Hình 1, đi từ Git căn bản đến cộng
tác và tự động hóa.
Git căn bản Git nâng cao GitHub, GitLab CI/CD nhóm
học tiếp cộng tác tự động
Hình 1: Lộ trình đọc báo cáo từ Git căn bản đến quy trình nhóm
Bạn đọc đã quen Git có thể đọc lướt Chương 2 và đi thẳng vào Chương 3, nhưng tuyệt
đối không nên bỏ qua Chương 7 vì đó là nơi mọi kiến thức được ráp lại thành quy trình
nhóm hoàn chỉnh. Chương tiếp theo sẽ bắt đầu với Git căn bản, đúng điểm khởi đầu của
lộ trình trên.
2 Git căn bản
Git là hệ thống quản lý phiên bản phân tán phổ biến nhất hiện nay, được dùng làm nền
tảng cho toàn bộ quy trình nhóm trong học phần ASPX: từ lưu trữ source code Web
Forms, review bài qua pull request, đến tự động build project .NET Framework 4.8.1 trên
GitHub Actions và GitLab CI. Hiểu đúng bản chất phân tán của Git giúp sinh viên tránh
các lỗi kinh điển như ghi đè code của nhau, mất lịch sử sửa file Web.config, hay đẩy
nhầm connection string lên kho chứa chung [2].
Chương này gồm ba phần. Mục 2.1 ôn lại lịch sử ra đời của Git và lý do mô hình phân
tán thắng thế trước SVN hay CVS. Mục 2.2 mổ xẻ kiến trúc ba vùng và cấu trúc thư
mục .git. Mục 2.3 hướng dẫn cài đặt Git trên ba hệ điều hành và cấu hình chuẩn cho
một project ASPX mới.
13

---

## [Page 15] (`page-15.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
2.1 Lịch sử Git và mô hình phân tán
Git ra đời năm 2005 khi Linus Torvalds, tác giả nhân Linux, cần một công cụ quản lý
phiên bản mới cho kernel sau khi dự án ngừng sử dụng hệ thống độc quyền BitKeeper.
Yêu cầu đặt ra rất khắt khe: tốc độ cực nhanh với kho chứa hàng chục nghìn file, hỗ trợ
hàng trăm nhánh phát triển song song, bảo đảm toàn vẹn dữ liệu tuyệt đối, và cho phép
làm việc phân tán hoàn toàn [2]. Chỉ trong vài tuần, Torvalds đã hiện thực nhân đầu tiên
của Git, rồi cộng đồng kernel tiếp tục hoàn thiện thành công cụ chuẩn mực như ngày nay.
Bốn mục tiêu thiết kế cốt lõi của Git có thể tóm tắt như sau:
• Tốc độ: mọi thao tác thường dùng như xem lịch sử, so sánh phiên bản hay chuyển
nhánh đều chạy cục bộ, nhanh hơn hẳn mô hình phải hỏi máy chủ qua mạng.
• Thiết kế đơn giản mà tin cậy: dữ liệu được mô hình hóa thành đồ thị các đối tượng
bất biến, mỗi đối tượng định danh bằng mã băm SHA-1 của chính nội dung của nó.
• Hỗ trợ phát triển phi tuyến tính: tạo nhánh gần như tức thời, khuyến khích mỗi
tính năng hay mỗi bản sửa lỗi đi trên một nhánh riêng rồi hợp nhất lại.
• Phân tán hoàn toàn: không có khái niệm máy khách yếu, mọi bản sao đều là một
kho chứa đầy đủ, ngang hàng với nhau.
Điểm khác biệt căn bản giữa Git và các hệ thống tập trung như CVS hay SVN nằm ở
chỗ đặt lịch sử. Với SVN, lịch sử duy nhất nằm trên máy chủ: muốn xem một phiên bản
cũ hay tạo nhánh, máy trạm bắt buộc phải kết nối mạng. Với Git, lệnh git clone tải về
toàn bộ lịch sử, nên sinh viên có thể commit, tạo nhánh, xem log hay so sánh khác biệt
ngay cả khi mất mạng trong phòng lab. Mỗi bản sao vì thế vừa là môi trường làm việc,
vừa là một bản backup sống của cả dự án.
Với đồ án ASPX của nhóm ba người, tính phân tán mang lại ba lợi ích trực tiếp. Thứ
nhất, mỗi thành viên tự do commit nháp trên máy cá nhân rồi mới đẩy lên kho chứa
chung khi code đã chạy. Thứ hai, nhóm có thể gắn nhiều remote song song, ví dụ vừa đẩy
lên GitHub để chạy Actions, vừa mirror sang GitLab để chạy pipeline dự phòng. Thứ ba,
rủi ro mất code vì hỏng một máy hay xóa nhầm kho chứa trên cloud giảm hẳn, vì bất kỳ
bản clone nào cũng đủ sức dựng lại toàn bộ lịch sử [1].
Bảng 2 tổng hợp sự khác nhau giữa Git và hai hệ thống tập trung tiêu biểu theo năm
tiêu chí quan trọng nhất [2].
14

---

## [Page 16] (`page-16.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Tiêu chí Git SVN và CVS
Mô hình lưu trữ Phân tán: mỗi bản sao
chứa toàn bộ lịch sử và
metadata
Tập trung: lịch sử duy
nhất nằm trên máy chủ
Làm việc ngoại
tuyến
Đầy đủ: commit,
branch, log, diff đều
chạy cục bộ
Hạn chế: hầu hết thao
tác cần kết nối máy chủ
Nhánh và hợp
nhất
Nhánh cực nhẹ, tạo
trong tích tắc; merge là
việc hằng ngày
Nhánh nặng nề, merge
tốn kém và dễ phát sinh
lỗi
Toàn vẹn dữ liệu Mọi đối tượng băm
SHA-1, đổi một byte là
lộ ngay
Kiểm tra toàn vẹn yếu
hơn, dễ lệch phiên bản
Tốc độ thao tác Rất nhanh nhờ làm việc
cục bộ và nén hiệu quả
Chậm hơn do phụ
thuộc mạng và tải máy
chủ
Bảng 2: So sánh Git với SVN và CVS theo năm tiêu chí
Tóm lại, Git thắng thế không chỉ vì miễn phí hay phổ biến, mà vì mô hình phân tán
khớp với cách làm phần mềm hiện đại: phát triển song song, review chéo qua mạng, tích
hợp liên tục. Nắm được tinh thần này, sinh viên sẽ thấy các lệnh ở mục tiếp theo không
còn là thao tác rời rạc mà là những bước di chuyển dữ liệu có chủ đích giữa ba vùng của
Git.
2.2 Kiến trúc 3 vùng và thư mục .git
Mọi file trong project Git luôn nằm ở một trong ba vùng. Working Directory là thư
mục làm việc mà sinh viên nhìn thấy và sửa trực tiếp trong Visual Studio, ví dụ các file
Default.aspx, code-behind C# hay Web.config. Staging Area, còn gọi là Index, là vùng
đệm liệt kê chính xác những thay đổi sẽ đi vào phiên bản kế tiếp. Repository là cơ sở dữ
liệu lịch sử nằm trong thư mục .git, nơi mỗi phiên bản được lưu bất biến dưới dạng một
commit gắn với mã băm SHA-1.
Luồng dữ liệu chuẩn chỉ gồm hai bước. Lệnh git add chép nội dung đã chọn từ
Working Directory lên Staging Area. Lệnh git commit đóng gói toàn bộ Staging Area
thành một commit mới trong Repository và gắn nhãn tác giả, thời điểm, thông điệp.
Hình 2 minh họa luồng hai bước này cùng thao tác checkout đưa nội dung từ Repository
trở lại Working Directory khi cần quay về phiên bản cũ.
15

---

## [Page 17] (`page-17.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Working
Directory
Staging
Area
Repository
.git
add commit
checkout
Hình 2: Luồng dữ liệu giữa ba vùng trong Git
Điểm hay nhất của Staging Area là cho phép commit từng phần: sinh viên sửa hai chức
năng trong cùng một file nhưng vẫn có thể đưa từng phần lên Index bằng lệnh git add -p
rồi tạo hai commit gọn gàng với hai thông điệp khác nhau. Lệnh git status cho biết
file nào đang nằm ở vùng nào, còn lệnh git diff so sánh Working Directory với Staging
Area trong khi git diff --staged so sánh Staging Area với commit gần nhất. Thói
quen đọc kỹ output của git status trước mỗi commit giúp tránh đưa nhầm file rác như
bin, obj hay packages vào lịch sử.
Để thấy ba vùng bằng mắt thường, sinh viên chỉ cần mở project ASPX mẫu đã khởi
tạo Git rồi liệt kê thư mục .git như trong Liệt kê 1. Mọi chú thích trong khối lệnh đều
viết không dấu theo đúng quy định ASCII của môi trường liệt kê.
1 cd AspxDemo - NET481
2 ls . git
3 # output : HEAD config description hooks index info logs objects
refs
4 cat . git / HEAD
5 # output : ref : refs / heads / main
6 cat . git / config
7 # output shows remote origin url and branch main settings
8 git status -- short
9 git log -- oneline -5
Listing 1: Khám phá thư mục .git trong project ASPX mẫu
Ý nghĩa của từng thành phần chính trong thư mục .git như sau:
objects Kho chứa toàn bộ dữ liệu nội dung dưới dạng blob, tree và commit, mỗi đối
tượng đặt tên theo mã băm SHA-1 của chính nó.
refs Các con trỏ nhẹ trỏ tới commit: refs/heads giữ đầu các nhánh local còn refs/tags
giữ các thẻ phiên bản.
HEAD Con trỏ đặc biệt cho biết nhánh hiện tại đang checkout, thường là tham chiếu
dạng ref: refs/heads/main.
config File cấu hình riêng của kho chứa: địa chỉ remote, nhánh mặc định, thông tin người
dùng ghi đè cấu hình toàn cục.
16

---

## [Page 18] (`page-18.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
index File nhị phân hiện thực Staging Area, ghi lại chính xác nội dung sẽ đi vào commit
kế tiếp.
logs Nhật ký di chuyển của HEAD và các nhánh, là dữ liệu thô để lệnh reflog cứu hộ
commit tưởng đã mất.
hooks Thư mục chứa script mẫu kích hoạt trước hoặc sau các sự kiện như commit và
push, dùng để kiểm tra code tự động.
Xét ví dụ cụ thể với project ASPX: sinh viên sửa chuỗi kết nối trong file Web.config
rồi chạy lệnh git add Web.config. Lúc này Git băm nội dung mới, lưu một blob vào
objects và ghi đường dẫn vào index, nhưng con trỏ refs/heads/main vẫn đứng yên.
Khi chạy tiếp lệnh git commit -m "docs: sua chuoi ket noi co so du lieu", Git
tạo một commit mới trỏ về commit cha trước đó rồi dời refs/heads/main tới commit
vừa tạo. Nhờ đó lịch sử luôn là một chuỗi có thể truy vết ngược, và thao tác git log chỉ
đơn giản là đi ngược từ HEAD về quá khứ [2].
Một lưu ý thực hành: thư mục .git chính là toàn bộ kho chứa, nên chép cả thư mục
project kèm .git sang máy khác tương đương với clone đầy đủ lịch sử. Ngược lại, xóa
thư mục .git đồng nghĩa với việc bỏ quản lý phiên bản và mất toàn bộ lịch sử local, vì
vậy tuyệt đối không xóa khi chưa đẩy code lên remote. Quy tắc này đặc biệt quan trọng
trước mỗi buổi demo, khi sinh viên hay dọn dẹp thư mục một cách vội vàng.
2.3 Cài đặt và cấu hình đầu tiên
Trước khi cài mới, sinh viên nên kiểm tra Git đã có sẵn chưa bằng lệnh git --version.
Nếu máy báo nhận diện được phiên bản từ 2.x trở lên thì có thể dùng ngay. Nếu chưa có,
cách nhanh nhất là tải bộ cài chính thức từ trang chủ tại https://git-scm.com hoặc
dùng trình quản lý gói của từng hệ điều hành như trong Liệt kê 2. Trên Windows, bộ cài
Git for Windows đi kèm công cụ Git Bash mô phỏng môi trường dòng lệnh Linux, rất
tiện để chạy thống nhất mọi ví dụ trong báo cáo này.
1 # Windows ( PowerShell , dung winget )
2 winget install -- id Git . Git -e -- source winget
3 # Windows ( lua chon khac voi Chocolatey )
4 choco install git -y
5 # Ubuntu / Debian
6 sudo apt update && sudo apt install -y git
7 # Fedora
8 sudo dnf install -y git
9 # macOS ( dung Homebrew )
10 brew install git
11 # kiem tra phien ban sau khi cai
17

---

## [Page 19] (`page-19.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
12 git -- version
Listing 2: Cài đặt Git trên Windows, Linux và macOS
Cài xong, việc bắt buộc đầu tiên là khai báo danh tính, vì mỗi commit Git đều ghi
vĩnh viễn tên và email của tác giả. Sinh viên nên dùng họ tên thật và email trường
cấp để giảng viên đối chiếu công sức đóng góp khi chấm điểm dựa trên lịch sử commit.
Hai khóa cấu hình toàn cục user.name và user.email phục vụ đúng mục đích này, còn
init.defaultBranch đặt tên nhánh mặc định là main cho mọi kho chứa mới, thống nhất
với quy ước hiện hành của GitHub và GitLab.
Với project ASPX trên .NET Framework 4.8.1 [10], khóa core.autocrlf cũng rất
đáng quan tâm. Visual Studio trên Windows lưu file văn bản với ký tự xuống dòng
CRLF, trong khi kho chứa Git chuẩn hóa về LF để tránh nhiễu khi so sánh khác biệt.
Đặt core.autocrlf thành true trên Windows giúp Git tự chuyển đổi hai chiều một cách
trong suốt, còn trên Linux và macOS nên đặt input để chỉ chuẩn hóa khi commit2
.
Liệt kê 3 minh họa toàn bộ quy trình cấu hình lần đầu, khởi tạo kho chứa trống bằng
lệnh git init và nhân bản một kho chứa có sẵn bằng lệnh git clone.
1 git config -- global user . name " Nguyen Van A "
2 git config -- global user . email " nguyenvana@example . com "
3 git config -- global init . defaultBranch main
4 git config -- global core . autocrlf true
5 git config -- global -- list
6 mkdir AspxDemo - NET481
7 cd AspxDemo - NET481
8 git init
9 git status
10 cd ..
11 git clone https :// github . com / example - org / AspxDemo - NET481 . git
12 cd AspxDemo - NET481
13 git log -- oneline -3
14 git remote -v
Listing 3: Cấu hình đầu tiên, khởi tạo và nhân bản kho chứa
Hai lệnh cuối trong liệt kê trên đại diện cho hai cách bắt đầu khác nhau nhưng bổ trợ
cho nhau. Lệnh git init tạo một kho chứa hoàn toàn mới: Git sinh thư mục .git rỗng
với nhánh mặc định main và chưa có commit nào, phù hợp khi nhóm khởi động project
ASPX từ con số không trong Visual Studio. Lệnh git clone ngược lại tải về toàn bộ lịch
sử của một kho chứa đã tồn tại kèm remote origin trỏ về địa chỉ gốc, phù hợp khi thành
viên mới gia nhập nhóm giữa chừng.
2Trên Windows dùng giá trị true, trên Linux và macOS dùng giá trị input; không bao giờ đặt false
cho project nhóm vì mỗi thành viên sẽ sinh ra diff rác do khác ký tự xuống dòng.
18

---

## [Page 20] (`page-20.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Ý nghĩa chi tiết của từng khóa cấu hình trong Liệt kê 3 như sau:
user.name Tên tác giả gắn vào mọi commit, nên đặt họ tên thật trùng với tên thành
viên trong file phân công nhóm.
user.email Email tác giả gắn vào mọi commit, nên dùng email trường cấp để đồng bộ
thống kê đóng góp trên GitHub và GitLab.
init.defaultBranch Tên nhánh khởi tạo cho kho chứa mới, đặt main để khớp với nhánh
mặc định của các dịch vụ cloud hiện nay.
core.autocrlf Chế độ chuẩn hóa ký tự xuống dòng, đặt true trên Windows và input
trên Linux hay macOS cho project nhóm.
2.3.1 Mức cấu hình và danh sách kiểm tra sau cài đặt
Git quản lý cấu hình theo ba mức xếp chồng. Mức system áp dụng cho mọi người dùng
trên máy, lưu trong file cài đặt chung của Git. Mức global áp dụng cho mọi kho chứa của
người dùng hiện tại, lưu trong file .gitconfig ở thư mục home. Mức local chỉ áp dụng
cho một kho chứa duy nhất, lưu trong file config của thư mục .git. Mức local thắng
global và global thắng system. Nhờ đó nhóm có thể đặt email trường học ở mức global,
rồi ghi đè email riêng cho một repo bằng lệnh git config user.email không kèm cờ
--global. Lệnh git config --list --show-origin liệt kê toàn bộ cấu hình hiệu lực
kèm file nguồn của từng dòng. Dòng nào bất ngờ đều truy được về đúng file để sửa, thay
vì đoán mò.
Sau khi chạy xong các lệnh cấu hình, sinh viên nên đi qua danh sách kiểm tra sau
trước khi bắt tay vào code:
1. Lệnh git --version in ra phiên bản 2.x. Chứng tỏ Git đã nằm trong biến môi
trường PATH và chạy được từ mọi thư mục.
2. Lệnh git config --global user.name và git config --global user.email trả
về đúng họ tên và email đã khai báo.
3. Lệnh git config --global init.defaultBranch trả về main. Bảo đảm kho chứa
mới không còn dùng tên nhánh cũ master.
4. Lệnh git config --global core.autocrlf trả về true trên Windows hoặc input
trên Linux và macOS.
5. Tạo thử một thư mục tạm, chạy git init rồi git status. Kết quả mong đợi là
thông báo nhánh main sạch, không báo lỗi.
19

---

## [Page 21] (`page-21.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Ngoài ra, sinh viên mới thường nhầm lẫn Git với GitHub. Git là công cụ quản lý phiên
bản chạy trên máy local, hoạt động tốt ngay cả khi không có mạng. GitHub và GitLab
là các dịch vụ lưu trữ và cộng tác trên cloud. Chúng cung cấp thêm pull request, review
code và pipeline CI [6] [8]. Hiểu đúng ranh giới này giúp nhóm phân công hợp lý. Thành
thạo Git local trước, rồi mới học cộng tác nhóm qua GitHub và GitLab ở các chương sau.
2.3.2 Commit đầu tiên cho project ASPX mẫu
Với kho chứa vừa khởi tạo, trình tự năm bước sau tạo nên commit đầu tiên đúng chuẩn
nhóm. Thứ nhất, tạo file solution và project Web Forms bằng Visual Studio 2022 với target
.NET Framework 4.8.1 theo đúng yêu cầu học phần [10]. Thứ hai, thêm file .gitignore
chuẩn cho ASP.NET. File này loại ngay các thư mục bin, obj, packages và thư mục .vs
khỏi tầm theo dõi của Git. Thứ ba, chạy lệnh git status để đọc danh sách file Git đề
xuất. Cần kiểm tra không còn file rác hay file chứa secret trước khi đi tiếp. Thứ tư, chạy
lệnh git add -A để đưa toàn bộ file hợp lệ lên Staging Area. Chạy lại git status để
xác nhận vùng đệm đúng ý. Thứ năm, chạy lệnh commit kèm thông điệp rõ ràng, ví dụ
git commit -m "feat: khoi tao project ASPX 4.8.1". Kiểm tra kết quả bằng lệnh
git log --oneline và git show --stat.
Một kiểm tra nâng cao sau commit đầu tiên là xác nhận ký tự xuống dòng đã chuẩn
hóa đúng. Lệnh git ls-files --eol liệt kê từng file kèm định dạng trong Working
Directory và trong Index. Nếu cột Index toàn lf trong khi cột Working Directory hiển
thị crlf trên máy Windows thì cấu hình core.autocrlf đã đúng. Commit đầu tiên chỉ
nên gồm file solution, file project và .gitignore. Tuyệt đối chưa đưa thư mục bin hay
obj vào lịch sử. Từ commit thứ hai trở đi, mỗi thay đổi logic đi kèm một commit riêng
với thông điệp mô tả đúng việc đã làm. Thói quen này tạo tiền đề cho kỹ thuật nhánh
và review code ở các chương sau.
2.3.3 Ghi nhớ credential và ba lỗi cấu hình phổ biến
Khi clone và đẩy code qua HTTPS, Git hỏi username và mật khẩu ở lần đầu tiên.
Trên GitHub hiện nay, mật khẩu tài khoản không còn dùng được cho Git qua HTTPS.
Sinh viên phải tạo Personal Access Token và dùng token thay cho mật khẩu. Lệnh
git config --global credential.helper manager bật kho credential của hệ điều hành
để chỉ nhập token một lần duy nhất.
Ba lỗi cấu hình phổ biến nhất của sinh viên năm nhất như sau:
• Quên khai báo danh tính nên commit gắn email mặc định của máy, khiến thống kê
đóng góp trên GitHub không nhận ra tác giả. Cách sửa là khai báo lại user.name và
user.email, rồi sửa commit gần nhất bằng git commit --amend --reset-author.
• Đặt core.autocrlf thành false khiến mỗi thành viên sinh ra diff rác do khác ký
20

---

## [Page 22] (`page-22.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
tự xuống dòng. Cách sửa là đặt lại đúng giá trị theo hệ điều hành rồi chuẩn hóa
kho chứa bằng git add --renormalize ..
• Clone bằng địa chỉ SSH khi chưa tạo SSH key nên Git báo lỗi quyền truy cập. Cách
đơn giản nhất cho người mới là dùng địa chỉ HTTPS kèm Personal Access Token
thay vì SSH.
Ghi nhớ ba lỗi trên giúp buổi lab đầu tiên trôi chảy, không ai bị kẹt ở bước đăng nhập
hay commit lỗi tác giả.
Sau khi cấu hình xong, sinh viên nên kiểm tra lại bằng lệnh git config --global --list
và chạy thử một vòng đời đầy đủ: tạo file Default.aspx đơn giản, rồi thực hiện lần lượt
git status, git add, git commit và git log để cảm nhận dữ liệu di chuyển qua ba
vùng như Hình 2. Vòng đời này chính là nhịp làm việc hằng ngày trong suốt đồ án: sửa
code, chọn thay đổi, đóng gói commit, đẩy lên remote để đồng đội review. Các mục tiếp
theo của báo cáo sẽ xây dựng toàn bộ kỹ thuật nhánh, hợp nhất và cộng tác nhóm dựa
trên nền tảng vững chắc này.
2.4 Vòng đời file và commit đầu tiên
Git theo dõi mỗi file trong kho chứa thông qua bốn trạng thái của vòng đời file, như minh
họa ở Hình 3. Hiểu đúng vòng đời này giúp sinh viên không bao giờ mất bài do nhầm lẫn
giữa file chưa lưu vào vùng stage và file đã commit [2]. Ba vùng dữ liệu tương ứng là thư
mục làm việc, vùng stage (còn gọi là index) và kho chứa gồm các commit [1].
Untracked File mới mà Git chưa quản lý, ví dụ trang About.aspx vừa tạo trong project.
File untracked không xuất hiện trong lịch sử commit cho đến khi được đưa vào stage
lần đầu.
Modified File đã tracked nhưng bị sửa đổi trong thư mục làm việc mà chưa đưa vào
stage.
Staged File đã được git add và nằm trong index, sẵn sàng cho commit kế tiếp.
Committed Dữ liệu đã nằm an toàn trong kho chứa dưới dạng một commit có mã băm
SHA-1 duy nhất.
Untracked Modified Staged Committed
add add commit
edit
Hình 3: Vòng đời của file trong Git từ chưa theo dõi đến đã commit
21

---

## [Page 23] (`page-23.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Lệnh git status cho biết trạng thái hiện tại của từng file, còn git add chuyển file
sang vùng stage. Dạng rút gọn git status --short rất tiện khi làm bài: hai cột ký
tự đầu dòng thể hiện trạng thái của index và của thư mục làm việc. Ví dụ ?? nghĩa là
untracked, A nghĩa là đã add, M nghĩa là đã sửa đổi. Quy trình chuẩn cho commit đầu
tiên của project ASPX gồm bốn bước trong Khối lệnh dưới đây.
1 # 1. Init a Git repo inside the ASPX project folder
2 git init AspxDemo_NET481
3 cd AspxDemo_NET481
4
5 # 2. Local identity for this repo only
6 git config user . name " Nguyen Van A "
7 git config user . email " nva@student . edu . vn "
8
9 # 3. Create a simple ASPX page , then check status
10 echo ’ <% @ Page Language =" C #" % > ’ > Default . aspx
11 echo ’ < html > < body > Hello ASPX </ body > </ html > ’ >> Default . aspx
12 git status -- short
13 # Output : ?? Default . aspx ( untracked )
14
15 # 4. Stage the file , then commit
16 git add Default . aspx
17 git status -- short
18 # Output : A Default . aspx ( staged )
19
20 git commit -m " feat : add Default . aspx homepage skeleton "
21 git log -- oneline -1
22
23 # 5. Edit the file -> modified ( unstaged )
24 echo ’ <! - - header --> ’ >> Default . aspx
25 git status -- short
26 # Output : M Default . aspx ( modified )
27
28 # 6. Forgot a file ? Stage it and fold into the last commit
29 echo ’ <% @ Master Language =" C #" % > ’ > Site . Master
30 git add Default . aspx Site . Master
31 git commit -- amend --no - edit
32 git log -- oneline -1
33 git status -- short
Tùy chọn --amend viết lại commit mới nhất bằng cách thay cây file và thông điệp
của nó, thay vì tạo commit mới. Lệnh này chỉ an toàn khi commit chưa được push lên
22

---

## [Page 24] (`page-24.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
kho chứa chung, vì nó thay đổi mã băm của commit [2]. Với project bài tập, nhóm nên
viết thông điệp commit theo chuẩn Conventional Commits, ví dụ feat: ..., fix: ...,
docs: ... [3]. Thông điệp tốt giúp giảng viên đọc lịch sử là hiểu ngay tiến độ: trang nào
đã xong, lỗi nào đã sửa, tài liệu nào đã cập nhật. Một quy ước gợi ý cho đồ án Web Forms
là mỗi commit chỉ đụng một trang hoặc một UserControl, kèm thông điệp nêu rõ tên file
đã đổi.
2.5 Xem lịch sử và so sánh
Ba nhu cầu phổ biến nhất khi đọc lịch sử là xem danh sách commit, xem chi tiết một
commit và so sánh các phiên bản với nhau. Lệnh git log hiển thị lịch sử, lệnh git show
hiển thị chi tiết, còn lệnh git diff hiển thị sự khác biệt giữa hai trạng thái [2]. Bảng 3
tóm tắt các tùy chọn mà sinh viên dùng hằng ngày khi làm bài tập nhóm.
Bảng 3: Các lệnh xem lịch sử và so sánh dùng hằng ngày
Mục đích Lệnh Ghi chú
Lịch sử rút gọn git log –oneline Mỗi commit một dòng
Sơ đồ nhánh git log –graph –all Nên kèm –oneline –decorate
Chi tiết một commit git show + mã băm Gồm metadata và patch
So sánh chưa stage git diff Thư mục làm việc so với index
So sánh đã stage git diff –staged Index so với HEAD
Thống kê file đổi git diff –stat Gọn, dùng khi review
Tùy chọn --oneline nén mỗi commit thành một dòng gồm bảy ký tự đầu của mã băm
và dòng tiêu đề của thông điệp. Kết hợp ba tùy chọn log --oneline --graph --all
cho ra sơ đồ ASCII thể hiện đầy đủ các nhánh và điểm rẽ, điểm hợp nhất. Lệnh git show
không tham số sẽ hiển thị commit mới nhất, còn khi kèm mã băm thì hiển thị đúng
commit đó. Thêm tên file ở cuối, ví dụ git show a1b2c3d -- Default.aspx, để chỉ
xem thay đổi trên file quan tâm.
1 # Compact history , newest first
2 git log -- oneline -5
3 # a1b2c3d feat : add login form validation
4 # 9 f8e7d6 fix : correct Web . config debug flag
5 # 4 c3b2a1 docs : update README build steps
6 # 77 aa11b feat : add cart UserControl
7 # 2 e1f0c9 init : scaffold ASPX Web Forms project
8
9 # Graph of all branches with decorations
10 git log -- oneline -- graph -- all -- decorate -8
23

---

## [Page 25] (`page-25.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
11 # * a1b2c3d ( HEAD -> main ) feat : add login form validation
12 # | * 88 bb22c ( feature / cart ) feat : add cart UserControl
13 # |/
14 # * 9 f8e7d6 fix : correct Web . config debug flag
15 # * 4 c3b2a1 docs : update README build steps
16
17 # Show one commit in detail ( metadata + patch )
18 git show -- stat HEAD
19 git show a1b2c3d -- Default . aspx
Lệnh git diff không tham số so sánh thư mục làm việc với vùng stage, tức chỉ
hiện thay đổi chưa được add. Muốn xem thay đổi đã add nhưng chưa commit, bắt
buộc phải thêm --staged (hoặc --cached, hai tên tương đương). Ký hiệu hai chấm
main..feature/cart so sánh đầu nhánh này với đầu nhánh kia, rất tiện trước khi hợp
nhất hoặc nộp pull request. Đoạn patch trong output dùng dấu cộng cho dòng thêm và
dấu trừ cho dòng xóa, kèm tiêu đề hunk dạng @@ -1,2 +1,3 @@.
1 # Unstaged changes : working tree vs index
2 git diff
3 # diff -- git a / Default . aspx b / Default . aspx
4 # --- a / Default . aspx
5 # +++ b / Default . aspx
6 # @@ -1 ,2 +1 ,3 @@
7 # <% @ Page Language =" C #" % >
8 # + <! - - header -->
9 # < html > < body > Hello ASPX </ body > </ html >
10
11 # Staged changes : index vs HEAD
12 git add Default . aspx
13 git diff -- staged
14 git diff -- cached -- stat
15
16 # Compare branches or commits before merge or review
17 git diff main .. feature / cart -- stat
18 git diff HEAD ~1 HEAD -- Web . config
19 git diff -- word - diff Default . aspx
Một thói quen tốt là luôn chạy git diff --staged để rà soát lần cuối trước khi
commit, giống như đọc lại bài trước khi nộp. Với file Web.config chứa chuỗi kết nối,
bước rà soát này giúp phát hiện sớm mật khẩu thật bị lọt vào commit. Sinh viên nên tập
đọc patch thành thạo vì giao diện review trên GitHub và GitLab cũng hiển thị đúng định
dạng này [6].
24

---

## [Page 26] (`page-26.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
2.6 Hoàn tác thay đổi
Git phân biệt ba tầng có thể hoàn tác: commit đã tạo, vùng stage và thư mục làm việc.
Năm lệnh hoàn tác phổ biến gồm ba chế độ của git reset, cộng thêm git revert và
git restore. Bảng 4 so sánh tác động của từng lệnh để sinh viên chọn đúng công cụ cho
từng tình huống [2].
Bảng 4: So sánh các lệnh hoàn tác thay đổi trong Git
Lệnh Tác động An toàn trên nhánh chung Khi dùng
reset –soft Dời HEAD, giữ index và file Không Gộp commit cục bộ chưa push
reset –mixed Dời HEAD và index, giữ file Không Bỏ stage hàng loạt
reset –hard Dời cả ba, mất sửa đổi Không, xem cảnh báo Xóa sạch nháp cục bộ
revert Tạo commit mới đảo ngược Có Hoàn tác commit đã push
restore Chỉ sửa file, không đụng lịch sử Có Hủy sửa chưa commit
Cảnh báo: tuyệt đối không dùng git reset --hard hay git push --force trên
nhánh chung như main hoặc develop. Hai lệnh này viết lại lịch sử công khai, khiến đồng
đội bị mất commit hoặc phải xử lý xung đột không đáng có [1]. Quy tắc ngón tay cái là
lịch sử đã push thì chỉ được sửa bằng commit mới, tức dùng git revert thay vì reset.
Ngoại lệ duy nhất cho --hard là dọn dẹp nháp hoàn toàn cục bộ, khi chắc chắn không
ai khác có các commit đó. Trước mọi lệnh nguy hiểm, hãy tạo nhánh dự phòng bằng
git branch backup-ten-ngay để luôn có đường quay lại.
1 # --- git restore : undo files , history untouched ---
2 git restore Default . aspx # discard unstaged edits
3 git restore -- staged Default . aspx # unstage , keep edits in
files
4 git restore -- source = HEAD ~1 Web . config # take file from old
commit
5
6 # --- git reset : move HEAD ( local drafts only ) ---
7 git reset -- soft HEAD ~1 # keep index + working tree
8 git commit -m " feat : squash login + validation into one commit "
9 git reset -- mixed HEAD ~1 # keep working tree , reset index
10 git reset HEAD Default . aspx # unstage one file ( mixed is default
)
11
12 # --- git revert : safe undo on shared branches ---
13 git log -- oneline -3
14 git revert HEAD --no - edit # new commit that undoes HEAD
15 git revert --no - commit 9 f8e7d6 # stage a revert , commit later
25

---

## [Page 27] (`page-27.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
16 git status -- short
17
18 # --- last resort : discard everything local ( see warning ) ---
19 git branch backup -2026 -05 -30 # safety branch first
20 git reset -- hard HEAD # drop all uncommitted changes
Lệnh git restore ra đời để tách bạch hai việc mà trước đây đều dồn vào git checkout:
lấy lại file và chuyển nhánh. Cú pháp git restore --source cho phép lấy nội dung file
từ bất kỳ commit nào mà không di chuyển HEAD. Lệnh git revert không xóa commit
cũ mà tạo commit mới có nội dung đảo ngược, nên lịch sử vẫn trung thực và đầy đủ. Khi
revert một commit hợp nhất, cần thêm -m 1 để chỉ rõ giữ lại phía nhánh chính [2]. Với
sinh viên mới học, thứ tự ưu tiên khi lỡ tay là restore trước, revert sau, và chỉ dùng
reset khi hiểu rõ tác động.
2.7 Stash và tag
Khi đang sửa dở một trang mà phải chuyển nhánh gấp để sửa lỗi nóng, lệnh git stash
cất tạm mọi thay đổi chưa commit vào ngăn xếp. Vùng làm việc trở lại sạch sẽ ngay lập
tức, và sinh viên có thể lấy lại công việc dở dang bất cứ lúc nào bằng git stash pop [2].
Ba thao tác dùng nhiều nhất là stash push để cất, stash list để liệt kê và stash pop
để lấy lại đồng thời xóa khỏi ngăn xếp. Nên kèm thông điệp bằng tùy chọn -m, nếu không
Git sẽ đặt tên mặc định khó phân biệt khi có nhiều mục stash.
1 # Stash unfinished work before switching branch
2 git status -- short
3 # M Default . aspx
4 # M Login . aspx
5 git stash push -m " wip : half - done login check "
6 git status -- short # clean again
7 git stash list
8 # stash@ {0}: wip : half - done login check
9
10 # Fix the hot bug on another branch , then come back
11 git switch hotfix - config
12 # ... edit Web . config , commit ...
13 git switch main
14 git stash pop # restore + drop stash@ {0}
15 git status -- short
16 git stash list
Cần phân biệt stash pop với stash apply: lệnh pop xóa mục stash sau khi lấy lại,
còn apply giữ lại bản copy. Nếu ngăn xếp có nhiều mục, chỉ rõ mục cần lấy bằng tên
26

---

## [Page 28] (`page-28.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
dạng stash@{0} hoặc stash@{1} ở cuối lệnh. Trường hợp stash chứa file mới hoàn toàn
(untracked), phải thêm tùy chọn -u thì Git mới cất cả các file đó.
Trong khi stash quản lý công việc tạm thời, tag dùng để đánh dấu các mốc quan trọng
như bản nộp bài hoặc bản phát hành. Git có hai loại tag: tag nhẹ (lightweight) chỉ là một
tên trỏ tới commit, còn tag annotated là một đối tượng đầy đủ có tác giả, ngày tháng và
thông điệp [2]. Với bài nộp môn học, nhóm nên dùng tag annotated để giảng viên kiểm
tra được ai đánh tag và nộp những gì. Quy ước tên gợi ý là v1.0, v1.1 cho các lần nộp,
kèm tiền tố lớp nếu giảng viên yêu cầu.
1 # Lightweight tag : just a name on a commit
2 git tag v1 .0 - btvn
3
4 # Annotated tag : recommended for course submissions
5 git tag -a v1 .0 -m " Nop bai lan 1: Web Forms chay duoc "
6 git show v1 .0 --no - patch # author , date , message
7 git tag -l " v1 .* " # list matching tags
8 git tag - n99 # list tags with messages
9
10 # Share tags with the remote ( tags are NOT pushed by default )
11 git push origin v1 .0 # push one tag
12 git push origin -- tags # push all tags
13 git ls - remote -- tags origin
Lưu ý quan trọng là lệnh git push mặc định không đẩy tag lên kho chứa chung, nên
phải push tag một cách tường minh. Muốn xóa tag nhầm tên, dùng git tag -d v1.0
cho tag cục bộ rồi git push origin :v1.0 để xóa tag trên remote. Trước giờ nộp bài,
cả nhóm nên thống nhất một commit chốt trên nhánh main, đánh tag annotated và kiểm
tra lại bằng git show. Việc kết hợp stash cho công việc dở dang và tag cho các mốc nộp
bài giúp quy trình nhóm ba người luôn gọn gàng và dễ truy vết.
2.8 Nhánh trong Git: con trỏ nhẹ và thao tác cơ bản
Trong Git, nhánh (branch) thực chất chỉ là một con trỏ nhẹ trỏ tới một commit cụ thể,
thay vì một bản sao toàn bộ mã nguồn như nhiều hệ thống cũ [2]. Mỗi commit lưu con
trỏ tới commit cha của nó, nên toàn bộ lịch sử của một nhánh chính là chuỗi commit
duyệt ngược được từ con trỏ nhánh. Nhờ thiết kế này, việc tạo nhánh trong Git gần như
tức thì và tốn rất ít dung lượng. Cách tổ chức này khuyến khích lập trình viên tạo nhánh
riêng cho từng tính năng nhỏ thay vì dồn mọi thứ lên một nhánh duy nhất.
Con trỏ đặc biệt HEAD cho biết nhánh nào đang được lấy ra làm việc (checked out).
Khi tạo commit mới, Git tự động dịch con trỏ của nhánh hiện tại tới commit vừa tạo,
còn HEAD vẫn bám theo nhánh đó [1]. Hiểu rõ quan hệ giữa HEAD, nhánh và commit giúp
27

---

## [Page 29] (`page-29.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
sinh viên tránh nhầm lẫn khi chuyển nhánh hoặc hợp nhất code.
Với project ASPX, nhóm nên thống nhất quy ước đặt tên nhánh ngay từ đầu: nhánh
tính năng bắt đầu bằng feature/, nhánh sửa lỗi bắt đầu bằng fix/, nhánh tài liệu bắt
đầu bằng docs/. Ví dụ, nhánh feature/login-aspx chứa chức năng đăng nhập cho trang
Web Forms, còn nhánh fix/webconfig-charset sửa lỗi font chữ trong tệp cấu hình. Quy
ước này giúp pull request ngắn gọn và pipeline kiểm thử chạy đúng phạm vi [4].
1 # List branches , star marks current branch
2 git branch
3 git status - sb
4 # Create and switch to feature branch ( classic way )
5 git checkout -b feature /login - aspx
6 # Modern equivalent , needs Git 2.23 or newer
7 git switch -c feature /login - aspx
8 # Work , then commit on the branch
9 git add Default . aspx Default . aspx . cs
10 git commit -m " feat : add login form to Default page "
11 # Switch back to main and list all branches
12 git switch main
13 git branch -a
14 # Delete merged branch safely ( - D forces delete )
15 git branch -d feature /login - aspx
Listing 4: Tạo và quản lý nhánh tính năng
Khối lệnh trên bao quát vòng đời điển hình của một nhánh: tạo nhánh bằng checkout -b
hoặc switch -c, commit công việc lên nhánh, quay về nhánh main rồi xóa nhánh đã hợp
nhất. Tùy chọn -d chỉ xóa khi nhánh đã được hợp nhất, trong khi -D xóa cưỡng bức và
có thể làm mất commit chưa merge. Bảng sau tóm tắt các lệnh hay dùng nhất khi làm
việc với nhánh trong bài tập nhóm.
Bảng 5: Các lệnh làm việc với nhánh
Lệnh Ý nghĩa
git branch Liệt kê các nhánh local
git branch -a Liệt kê cả nhánh local và remote
git checkout -b ten-nhanh Tạo nhánh mới và chuyển sang ngay
git switch ten-nhanh Chuyển sang nhánh đã có
git switch -c ten-nhanh Tạo nhánh mới và chuyển sang ngay
git branch -d ten-nhanh Xóa nhánh đã hợp nhất xong
git branch -D ten-nhanh Xóa cưỡng bức nhánh chưa hợp nhất
28

---

## [Page 30] (`page-30.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
C1 C2
C3
main
F1
F2
login-aspx
HEAD
commit
merge
Hình 4: Mô hình hai nhánh và phép hợp nhất
Hình trên minh họa nhánh main đi qua các commit C1, C2, C3 trong khi nhánh tính
năng rẽ ra từ C2 với hai commit F1, F2 rồi hợp nhất trở lại. Mô hình rẽ nhánh và hợp
nhất liên tục này là nền tảng của GitFlow và nhiều quy trình nhóm hiện đại [4]. Khi đã
quen tay với nhánh, bước tiếp theo là hiểu sâu cơ chế hợp nhất và cách xử lý xung đột.
2.9 Hợp nhất nhánh và giải quyết xung đột
Lệnh git merge hợp nhất lịch sử của một nhánh vào nhánh hiện tại, nhưng kết quả cụ
thể phụ thuộc vào hình dạng lịch sử [2]. Nếu nhánh hiện tại chưa có commit mới nào kể
từ điểm rẽ nhánh, Git chỉ cần trượt con trỏ tới trước, gọi là hợp nhất fast-forward. Ngược
lại, khi cả hai nhánh đều có commit mới, Git phải tạo một commit gộp (merge commit)
có hai commit cha. Trường hợp thứ hai gọi là hợp nhất ba bên (three-way merge) và là
dạng phổ biến nhất trong làm việc nhóm.
Bảng 6: So sánh hợp nhất fast-forward và three-way
Tiêu chí Fast-forward Three-way merge
Điều kiện Nhánh đích đứng yên từ điểm rẽ Cả hai nhánh cùng có commit mới
Lịch sử Tuyến tính, không commit gộp Có commit gộp với hai cha
Lệnh thường dùng git merge ten-nhanh git merge –no-ff ten-nhanh
Hoàn tác git reset về commit cũ git reset hoặc git revert
Phù hợp Nhánh cá nhân ngắn ngày Nhánh tính năng của cả nhóm
Xung đột (conflict) xảy ra khi hai nhánh sửa cùng một vùng của cùng một tệp và Git
không thể tự quyết định giữ bên nào. Để luyện tập, nhóm cố tình gây xung đột trên tệp
Web.config bằng cách cho hai nhánh sửa cùng khóa SiteName trong khối appSettings.
Khối lệnh sau tái hiện toàn bộ quá trình ngay trên máy cá nhân của sinh viên.
1 # Create feature branch and edit SiteName there
2 git switch -c feature /login - aspx
3 git commit - am " feat : rename site to shop on feature branch "
4 # Back on main , edit the SAME key differently
29

---

## [Page 31] (`page-31.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
5 git switch main
6 git commit - am " feat : rename site to portal on main "
7 # Merge feature branch , Git stops with CONFLICT
8 git merge feature /login - aspx
9 # Inspect status and leftover whitespace errors
10 git status - sb
11 git diff -- check
Listing 5: Gây xung đột có chủ đích trên tệp cấu hình
Sau lệnh hợp nhất, Git đánh dấu vùng xung đột trong Web.config bằng ba loại
dấu: <<<<<<< HEAD mở đầu vùng của nhánh hiện tại, ======= ngăn cách hai bên, và
>>>>>>> feature/login-aspx kết thúc vùng của nhánh được hợp nhất. Không bao giờ
commit nguyên các dấu này lên kho chung, vì tệp cấu hình sẽ hỏng và ứng dụng ASPX
không khởi động được. Khối dưới đây cho thấy nội dung tệp tại thời điểm đang xung đột.
1 <?xml version = " 1.0 " encoding = " utf -8 " ? >
2 < configuration >
3 < appSettings >
4 < <<<<<< HEAD
5 < add key = " SiteName " value = " AspxDemo Portal " / >
6 =======
7 < add key = " SiteName " value = " AspxDemo Shop " / >
8 >>>>>>> feature / login - aspx
9 </ appSettings >
10 </ configuration >
Listing 6: Đoạn tệp cấu hình đang xung đột
Các bước giải quyết xung đột chuẩn cho sinh viên gồm:
1. Mở Web.config, đọc kỹ cả hai phía của vùng xung đột để hiểu ý đồ của mỗi bên.
2. Giữ lại một phía hoặc viết lại nội dung gộp cả hai ý, rồi xóa sạch ba loại dấu xung
đột.
3. Chạy git diff --check để chắc chắn không còn dấu thừa hay khoảng trắng lỗi.
4. Đánh dấu đã giải quyết bằng git add Web.config rồi hoàn tất với git commit.
5. Kiểm tra lại bằng git status và git log --graph trước khi đẩy lên kho chung.
1 <?xml version = " 1.0 " encoding = " utf -8 " ? >
2 < configuration >
3 < appSettings >
4 < add key = " SiteName " value = " AspxDemo Portal " / >
30

---

## [Page 32] (`page-32.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
5 </ appSettings >
6 </ configuration >
Listing 7: Tệp cấu hình sau khi giải quyết xung đột
Nếu đang hợp nhất dở mà nhận ra mình thao tác nhầm nhánh, lệnh git merge --abort
sẽ hủy toàn bộ tiến trình và đưa cây làm việc về trạng thái trước khi merge. Sau khi hủy,
nên chạy git status để xác nhận mọi thứ sạch sẽ rồi mới thao tác lại [1]. Với xung đột
phức tạp, sinh viên có thể nhờ công cụ gộp bằng hình ảnh của Visual Studio hỗ trợ, nhưng
vẫn phải đọc hiểu từng vùng trước khi bấm chấp nhận.
2.10 Tệp .gitignore chuẩn cho dự án ASP.NET
Tệp .gitignore liệt kê các đường dẫn mà Git phải bỏ qua, giúp kho chứa mã nguồn gọn
nhẹ và tránh rò rỉ tệp của máy cục bộ [6]. Với project ASP.NET Web Forms, ít nhất năm
nhóm phải luôn bị bỏ qua: thư mục biên dịch bin/ và obj/, thư mục gói packages/, thư
mục cấu hình Visual Studio .vs/, và tệp tùy chọn người dùng *.user. Khối mẫu đầy đủ
dưới đây có thể sao chép nguyên văn vào mọi đồ án ASPX của môn học. Mỗi khối đều
có chú thích để sinh viên hiểu rõ tác dụng trước khi áp dụng.
1 # Build outputs , rebuilt by Visual Studio or MSBuild
2 bin /
3 obj /
4
5 # Visual Studio per - machine files
6 . vs /
7 *. user
8 *. suo
9
10 # NuGet packages , restored on build
11 packages /
12 *. nupkg
13
14 # Publish profiles may leak server paths
15 *. pubxml
16 PublishProfiles /
17
18 # OS junk and logs
19 Thumbs . db
20 . DS_Store
21 *. log
22 *. tmp
31

---

## [Page 33] (`page-33.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Listing 8: Mẫu gitignore đầy đủ cho ASP.NET Web Forms
Build Hai mục bin/ và obj/ loại bỏ toàn bộ kết quả biên dịch, vì chúng được tạo lại
sau mỗi lần build.
Visual Studio Nhóm .vs/, *.user và *.suo chứa trạng thái cửa sổ của từng máy,
không có giá trị chia sẻ cho cả nhóm.
NuGet Thư mục packages/ và *.nupkg rất nặng nên chỉ lưu danh sách gói, khi build
hệ thống sẽ khôi phục tự động.
Publish Hồ sơ phát hành có thể lộ đường dẫn máy chủ, vì vậy *.pubxml và PublishProfiles/
cần bị chặn triệt để.
Hệ điều hành Các tệp Thumbs.db, .DS_Store và *.log do hệ điều hành và công cụ tự
sinh, không liên quan tới mã nguồn.
Lưu ý quan trọng: .gitignore chỉ có tác dụng với tệp chưa được theo dõi. Nếu ai đó
đã commit nhầm bin/ lên kho chung, việc thêm quy tắc bỏ qua sau đó không xóa được
lịch sử cũ, và đây cũng là câu hỏi phản biện quen thuộc của giảng viên. Cách sửa là gỡ tệp
khỏi chỉ mục nhưng giữ lại trên đĩa bằng git rm --cached, rồi commit kèm .gitignore
mới như khối lệnh dưới đây.
1 # Check which rule ignores a path , if any
2 git check - ignore -v Default . aspx
3 # File was committed before gitignore existed
4 git ls - files | findstr " bin obj user "
5 # Untrack it , but keep the local copy on disk
6 git rm -- cached -r bin obj
7 git rm -- cached AspxDemo . csproj . user
8 # Commit the fix together with gitignore
9 git add . gitignore
10 git commit -m " fix : stop tracking build outputs and user files "
11 git status - sb
Listing 9: Gỡ tệp đã commit nhầm ra khỏi chỉ mục
2.11 Dự án mini với ASPX: tạo trang, commit và xem lịch sử
Để gắn kiến thức nhánh và hợp nhất với học phần, nhóm xây dựng một project mini
gồm đúng một trang Default.aspx và tệp code-behind Default.aspx.cs trên .NET
Framework 4.8.1 [10]. Trang hiển thị một nhãn chào mừng và một nút bấm, đủ để demo
32

---

## [Page 34] (`page-34.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
vòng đời chỉnh sửa, commit, rẽ nhánh và hợp nhất. Mọi chuỗi chữ trong ví dụ đều viết
không dấu để giữ mã nguồn hoàn toàn ASCII.
1 <% @ Page Title = " Trang chu " Language = " C # " AutoEventWireup = " true "
CodeBehind = " Default . aspx . cs " Inherits = " AspxDemo . _Default " % >
2 <! DOCTYPE html >
3 < html xmlns = " http: // www . w3 . org /1999/ xhtml " >
4 < head runat = " server " >
5 < title > AspxDemo Mini </ title >
6 </ head >
7 < body >
8 < form id = " form1 " runat = " server " >
9 < div >
10 < asp:Label ID= " lblMessage " runat = " server " Text = " Xin
chao ASP . NET " / >
11 < br / >
12 < asp:Button ID= " btnClick " runat = " server " Text = " Nhan
vao day " OnClick = " btnClick_Click " / >
13 </ div >
14 </ form >
15 </ body >
16 </ html >
Listing 10: Trang Default ASPX cho dự án mini
Chỉ thị Page ở dòng đầu khai báo ngôn ngữ C# và liên kết tới tệp code-behind
Default.aspx.cs qua thuộc tính CodeBehind. Hai điều khiển Label và Button đều có
runat="server" nên truy cập được từ code-behind. Khi bấm nút trên trình duyệt, sự
kiện btnClick_Click sẽ chạy trên máy chủ rồi trả HTML mới về cho người dùng.
1 using System ;
2 namespace AspxDemo
3 {
4 public partial class _Default : System . Web . UI . Page
5 {
6 protected void Page_Load ( object sender , EventArgs e )
7 {
8 if (! IsPostBack )
9 {
10 // First visit , show default greeting
11 lblMessage . Text = " Xin chao ASP . NET 4.8.1 " ;
12 }
13 }
14 protected void btnClick_Click ( object sender , EventArgs e )
33

---

## [Page 35] (`page-35.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
15 {
16 // Button click , update the label text
17 lblMessage . Text = " Ban vua nhan nut , chuc mung ! " ;
18 }
19 }
20 }
Listing 11: Tệp code-behind xử lý sự kiện nút bấm
Lớp _Default kế thừa từ trang Web Forms và xử lý hai sự kiện: Page_Load hiển thị lời
chào khi mở trang lần đầu, còn btnClick_Click đổi nội dung nhãn khi người dùng bấm
nút. Thuộc tính IsPostBack giúp phân biệt lần mở trang đầu tiên với các lần gửi biểu
mẫu về máy chủ. Sau khi lưu hai tệp, sinh viên chạy khối lệnh Git dưới đây để commit
rồi quan sát lịch sử phân nhánh.
1 # Stage the new page and commit on main
2 git add Default . aspx Default . aspx . cs Web . config
3 git commit -m " feat : create Default page with greeting button "
4 # Create branch , edit button text , commit there
5 git switch -c feature /login - aspx
6 git commit - am " feat : change button text on login branch "
7 # Merge back to main and view the graph
8 git switch main
9 git merge --no - ff feature /login - aspx -m " Merge branch ’ feature /
login - aspx ’ "
10 git log -- graph -- oneline -- decorate -n 6
11 # Sample output of the log command above
12 # * 9 f3a1c2 ( HEAD -> main ) Merge branch ’ feature / login - aspx ’
13 # |\
14 # | * 7 b2e4a1 feat : change button text on login branch
15 # | * 2 c1d8f0 feat : create Default page with greeting button
16 # |/
Listing 12: Commit dự án mini và xem lịch sử phân nhánh
Tùy chọn --graph vẽ sơ đồ phân nhánh bằng ký tự ASCII, còn --oneline và --decorate
giúp mỗi commit gọn trong một dòng kèm tên nhánh. Thông điệp commit tuân thủ Con￾ventional Commits với tiền tố feat: và docs: giúp lịch sử dễ đọc và dễ sinh ghi chú phát
hành [3]. Hoàn thành dự án mini này, sinh viên đã đủ kỹ năng chuyển sang các thao tác
nâng cao như hoàn tác, stash và gắn thẻ phiên bản.
34

---

## [Page 36] (`page-36.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
3 Git nâng cao và chuyên sâu
Khi đã thành thạo các lệnh Git cơ bản như khởi tạo kho, ghi nhận thay đổi và làm việc
với nhánh, bước tiếp theo là hiểu những gì diễn ra bên trong thư mục .git. Hiểu mô hình
đối tượng, đồ thị lịch sử, cơ chế tham chiếu và cách Git lưu trữ dữ liệu giúp người học
lý giải được mọi hành vi của Git thay vì học thuộc lòng từng lệnh. Với đồ án ASP.NET
Web Forms trên .NET Framework 4.8.1, kiến thức này đặc biệt hữu ích khi kho chứa
nhiều file như Default.aspx, Web.config hay các gói trong thư mục packages [10]. Nội
dung dưới đây trình bày bốn chủ đề cốt lõi: mô hình đối tượng, đồ thị DAG cùng refs và
HEAD, reflog với kỹ thuật khôi phục, cuối cùng là packfile và bảo trì kho [2].
3.1 Mô hình đối tượng: blob, tree, commit và tag
Git về bản chất là một hệ thống file có địa chỉ hóa theo nội dung, trên đó người ta xây
thêm lớp quản lý phiên bản. Mọi dữ liệu trong kho đều được lưu thành các đối tượng
nằm trong thư mục .git/objects, mỗi đối tượng được định danh bằng giá trị băm SHA-1
của chính nội dung của nó. Nhờ cách định danh này, hai file có nội dung giống hệt nhau
dù nằm ở hai dự án khác nhau vẫn chỉ cần một đối tượng duy nhất, còn chỉ cần đổi một
byte thì giá trị băm đã hoàn toàn khác.
Git định nghĩa bốn loại đối tượng cơ bản như sau:
• blob lưu nội dung thô của một file, không kèm tên file hay quyền hạn. Mỗi phiên
bản khác nhau của Web.config là một blob khác nhau.
• tree mô tả một thư mục: danh sách các mục con, mỗi mục gồm chế độ truy cập,
tên file hoặc tên thư mục con, và giá trị băm của blob hay tree tương ứng.
• commit ghi nhận một trạng thái của toàn bộ dự án: băm của tree gốc, băm của
commit cha, thông tin tác giả, thời gian và thông điệp commit.
• tag dạng annotated là một đối tượng độc lập trỏ tới một commit, kèm theo tên tag,
người tạo, ngày tháng và thông điệp, thường dùng để đánh dấu các bản phát hành
như bản nộp đồ án.
Bảng 7 tóm tắt vai trò của từng loại đối tượng cùng lệnh truy vấn tương ứng.
Bảng 7: Cac loai doi tuong co ban trong Git
Loại đối tượng Nội dung lưu trữ Câu lệnh truy vấn thường gặp
blob Nội dung một phiên bản của file Xem nội dung blob theo băm
tree Danh sách các mục con của thư mục Liệt kê cây thư mục gốc
commit Trạng thái dự án và liên kết tới commit cha Xem chi tiết một commit
tag Nhãn định danh gắn với một commit Liệt kê và xem nội dung tag
35

---

## [Page 37] (`page-37.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Vì sao chỉ đổi một byte cũng đổi toàn bộ giá trị băm? Nguyên nhân nằm ở cách Git
tính băm: với mỗi đối tượng, Git ghép chuỗi đầu gồm loại đối tượng và kích thước, thêm
một byte rỗng, rồi nối tiếp nội dung thô, sau đó băm SHA-1 toàn bộ khối dữ liệu đó.
Thuật toán băm có hiệu ứng lan truyền, nghĩa là thay đổi nhỏ ở đầu vào tạo ra đầu ra
khác hẳn ở mọi vị trí, vì vậy không thể âm thầm sửa một file mà giữ nguyên giá trị băm
cũ. Mỗi lần đọc đối tượng, Git tính lại giá trị băm và so với tên file đang lưu, nên mọi hư
hỏng ổ đĩa hay can thiệp thủ công đều bị phát hiện ngay [2].
Hai lệnh quan trọng nhất để khám phá mô hình này là git cat-file -t để xem loại
đối tượng và git cat-file -p để in nội dung ở dạng dễ đọc. Khối lệnh dưới đây tạo một
kho thử nghiệm gắn với project Web Forms, ghi nhận hai file, rồi dùng hai lệnh trên để
mổ xẻ từng đối tượng.
1 # Create a demo repo that imitates a small ASPX project
2 mkdir DemoInternals && cd DemoInternals
3 git init -b main
4 git config user . name " Sinh Vien "
5 git config user . email " sinhvien@example . com "
6 printf ’ <%% @ Page Language =" C #" %% >\ n ’ > Default . aspx
7 echo " sample connection string " > Web . config
8 git add Default . aspx Web . config
9 git commit -m " feat : khoi tao project Web Forms demo "
10 # Show the type and the content of HEAD commit
11 git cat - file -t HEAD
12 git cat - file -p HEAD
13 # List the root tree and inspect one blob
14 TREE = $ ( git rev - parse HEAD ^{ tree })
15 git cat - file -p $TREE
16 BLOB = $ ( git rev - parse HEAD : Default . aspx )
17 git cat - file -t $BLOB
18 git cat - file -p $BLOB
19 # Prove that one changed byte gives a new hash
20 echo " X " >> Default . aspx
21 git hash - object Default . aspx
22 echo " Compare with the old hash stored in BLOB above "
Kết quả của git cat-file -p HEAD cho thấy commit chỉ là một bản ghi văn bản
gồm tree, parent, author, committer và message, hoàn toàn có thể đọc được bằng mắt
thường. Từ tree gốc, người đọc lần ra băm của từng blob, rồi dùng tiếp git cat-file -p
với băm đó để xem nội dung file tại đúng thời điểm commit, đó chính là cách Git tái hiện
toàn bộ dự án ở bất kỳ phiên bản nào. Thí nghiệm ở hai dòng cuối chứng minh tính nhạy
của hàm băm: file Default.aspx chỉ thêm một ký tự mà git hash-object đã cho ra giá
trị khác hẳn băm cũ lưu trong biến BLOB.
36

---

## [Page 38] (`page-38.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Một lưu ý thực tế cho đồ án ASPX: các file như Web.config thường xuyên thay đổi
connection string giữa các máy, mỗi lần đổi là một blob mới. Vì vậy nhóm nên tách cấu
hình thật ra khỏi kho bằng biến môi trường hoặc file mẫu, tránh để lịch sử phình to vì
những blob chứa chuỗi kết nối khác nhau mà giá trị thực tế không cần lưu [1].
3.2 Đồ thị DAG, refs và HEAD
Các commit trong Git liên kết với nhau thành một đồ thị có hướng không chu trình, gọi
tắt là DAG. Mỗi commit lưu băm của commit cha, commit merge lưu hai cha, nhờ đó
toàn bộ lịch sử là một mạng lưới mà từ bất kỳ commit nào cũng có thể lần ngược về
commit đầu tiên. Tính bất biến là điểm mấu chốt: một khi commit đã tạo thì không thể
sửa, mọi thao tác như hiệu chỉnh thông điệp hay gộp nhánh thực chất đều tạo commit
mới và dời con trỏ nhánh tới đó.
Nhánh trong Git chỉ là một con trỏ nhẹ, tức một file văn bản nằm trong .git/refs/heads
có tên trùng tên nhánh và nội dung là đúng 40 ký tự băm của commit đỉnh nhánh. Tạo
nhánh mới vì thế chỉ tốn một file vài chục byte, xóa nhánh cũng chỉ là xóa file đó,
toàn bộ commit vẫn còn nguyên trong kho cho tới khi bị thu gom rác. HEAD là con
trỏ đặc biệt cho biết vị trí làm việc hiện tại: ở trạng thái bình thường nó chứa dòng
ref: refs/heads/main, nghĩa là đang đứng trên nhánh main, còn ở trạng thái detached
HEAD thì nó chứa trực tiếp một giá trị băm.
Trạng thái detached HEAD xảy ra khi checkout trực tiếp một commit, một tag hay
một biểu thức như HEAD~2 thay vì checkout tên nhánh. Ở trạng thái này, commit mới
tạo ra không thuộc nhánh nào, nếu chuyển sang nhánh khác mà không lưu lại băm thì
rất khó tìm lại, cách xử lý đúng là tạo nhánh ngay bằng git switch -c cuu-ho hoặc
git branch cuu-ho. Hình 5 minh họa một DAG đơn giản: chuỗi commit A tới B tới C
trên nhánh main, cùng nhánh feature tách ra từ B và có thêm commit D.
A B C
D
parent parent
parent
nhanh main tro toi C
nhanh feature tro toi D
Hình 5: Do thi DAG voi chuoi commit A B C va hai nhanh
Khối lệnh sau giúp kiểm chứng trực tiếp rằng nhánh chỉ là file và HEAD chỉ là con
trỏ, hãy chạy trong kho DemoInternals vừa tạo ở trên.
1 # A branch is just a file holding a 40 - char hash
37

---

## [Page 39] (`page-39.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
2 cat . git / refs / heads / main
3 git rev - parse main
4 # HEAD points at the current branch in normal state
5 cat . git / HEAD
6 git symbolic - ref HEAD
7 git rev - parse -- abbrev - ref HEAD
8 # Create two commits , then look at them as a graph
9 echo " v2 " >> Default . aspx && git commit - am " feat : ban thu hai "
10 git switch -c feature
11 echo " v3 " >> Default . aspx && git commit - am " feat : thu nghiem
tren nhanh feature "
12 git log -- graph -- oneline -- all -n 6
13 git branch -v
14 # Enter detached HEAD on purpose , then go back safely
15 git switch -- detach HEAD ~1
16 git status - sb | head -n 3
17 git switch main
Ba lệnh đầu chứng minh file main trong refs/heads và lệnh git rev-parse main in
ra cùng một giá trị băm. git symbolic-ref HEAD in ra nhánh đang trỏ tới, còn ở trạng
thái detached thì lệnh này báo lỗi, đó là dấu hiệu phân biệt nhanh nhất giữa hai trạng
thái. Lệnh git log --graph --oneline --all vẽ lại đúng DAG như Hình 5 nhưng với
dữ liệu thật, mỗi dòng sao và đường gạch thể hiện một nút commit và cạnh nối tới commit
cha.
3.3 Reflog và khôi phục commit tưởng chừng đã mất
Reflog là nhật ký ghi lại mọi lần giá trị của HEAD hay của các nhánh thay đổi: mỗi lần
commit, checkout, reset, merge hay rebase đều để lại một dòng trong reflog. Dữ liệu này
nằm trong thư mục .git/logs và chỉ tồn tại ở máy cục bộ, không bao giờ được push
lên GitHub hay GitLab, vì vậy nó là lưới an toàn cho thao tác cá nhân chứ không phải
cơ chế sao lưu của nhóm. Theo mặc định, các mục reflog còn trỏ tới được giữ khoảng 90
ngày, các mục không còn trỏ tới được giữ khoảng 30 ngày, đủ dài để cứu hầu hết các tai
nạn thường gặp [1].
Tình huống kinh điển là chạy git reset --hard nhầm và tưởng rằng commit đã mất
vĩnh viễn. Thực ra lệnh đó chỉ dời con trỏ nhánh về commit cũ hơn, còn đối tượng commit
vẫn nằm nguyên trong kho, git log không hiện ra chỉ vì không còn đường nào từ nhánh
hiện tại tới được nó. Chỉ cần tìm lại giá trị băm trong git reflog rồi tạo nhánh hoặc
reset tới băm đó là khôi phục nguyên vẹn.
Các bước thực hiện cụ thể như sau:
1. Tạo một commit mới rồi cố ý reset cứng về commit trước đó để mô phỏng tai nạn.
38

---

## [Page 40] (`page-40.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
2. Chạy git reflog và xác định dòng ghi lại commit vừa mất, thường nằm ngay đầu
danh sách.
3. Tạo nhánh cứu hộ trỏ đúng vào băm của commit mất, sau đó kiểm tra file đã quay
lại đầy đủ.
4. Gộp hoặc cherry-pick commit cứu được về nhánh chính, cuối cùng xóa nhánh cứu
hộ tạm thời.
Khối lệnh dưới đây thực hiện đúng bốn bước trên trong kho DemoInternals.
1 # Step 1: make a commit , then lose it with a hard reset
2 echo " bao cao quan trong " > KetQua . txt
3 git add KetQua . txt && git commit -m " feat : them file ket qua "
4 LOST = $ ( git rev - parse HEAD )
5 echo " Lost commit hash : $LOST "
6 git reset -- hard HEAD ~1
7 git log -- oneline -n 3
8 # Step 2: the commit is gone from log , but reflog remembers it
9 git reflog -n 5
10 # Step 3: rescue it with a branch pointing at the saved hash
11 git branch cuu - ho $LOST
12 git switch cuu - ho
13 cat KetQua . txt
14 git log -- oneline -n 2
15 # Step 4: bring it back to main , then drop the rescue branch
16 git switch main
17 git merge --no - ff cuu - ho -m " merge : lay lai commit bi mat "
18 git branch -d cuu - ho
19 git log -- graph -- oneline -n 4
Nếu không nhớ băm và reflog đã quá dài, lệnh git fsck --lost-found sẽ quét toàn
bộ kho để liệt kê các commit không còn được tham chiếu tới, đây là phao cứu sinh cuối cùng
trước khi đối tượng bị xóa hẳn. Cần nhớ rằng reflog chỉ cứu được những commit đã từng
tồn tại trong kho cục bộ, các thay đổi chưa bao giờ được commit thì git reset --hard
sẽ xóa vĩnh viễn khỏi thư mục làm việc. Với đồ án ASPX, quy tắc an toàn rút ra là:
commit thường xuyên trước mỗi lần thử nghiệm cấu hình Web.config, và không bao giờ
reset cứng khi thư mục làm việc còn file chưa commit [2].
3.4 Packfile và bảo trì kho
Khi mới commit, mỗi đối tượng nằm rời rạc thành một file riêng trong .git/objects,
cách lưu này nhanh khi ghi nhưng tốn chỗ và chậm khi kho có hàng nghìn đối tượng. Git
39

---

## [Page 41] (`page-41.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
giải quyết bằng packfile: nhiều đối tượng được nén chung vào một file .pack kèm file chỉ
mục .idx trong thư mục .git/objects/pack. Điểm đặc biệt là Git không nén từng file
độc lập mà lưu các phiên bản gần giống nhau dưới dạng delta, tức chỉ lưu phần khác biệt
so với một phiên bản gốc, nhờ đó kho source code thường tiết kiệm tới 80% dung lượng
so với lưu rời rạc.
Ba lệnh bảo trì cần nắm vững là git count-objects -v để chẩn đoán, git gc để thu
gom và đóng gói, git prune để xóa đối tượng không còn được tham chiếu. Lệnh git gc
gọi tắt của garbage collector, thực hiện một loạt việc: nén các đối tượng rời rạc thành
packfile, gom các packfile nhỏ thành packfile lớn, xóa nhánh đã hợp nhất theo cấu hình,
và dọn các mục reflog hết hạn. Mặc định Git tự chạy git gc --auto sau các lệnh như
commit hay merge khi phát hiện kho có quá nhiều đối tượng rời rạc, vì vậy người dùng
phổ thông hiếm khi cần chạy thủ công.
Khối lệnh sau minh họa quy trình chẩn đoán và bảo trì trên kho DemoInternals.
1 # Diagnose : how many loose objects and packs exist
2 git count - objects -v
3 du - sh . git
4 # Force a full maintenance pass and compare afterwards
5 git gc
6 git count - objects -v
7 du - sh . git
8 # Inspect packs and verify the whole object database
9 ls . git / objects / pack /
10 git verify - pack -v . git / objects / pack /*. idx | head -n 5
11 git fsck -- full
12 # Aggressive repack for a release backup ( slow , rare use )
13 git gc -- aggressive -- prune = now
14 git count - objects -v
Kết quả git count-objects -v gồm các trường quan trọng: số đối tượng rời rạc,
số packfile, số đối tượng nằm trong pack, và dung lượng ước tính của kho. Sau lệnh
git gc, số đối tượng rời rạc thường về 0 trong khi số đối tượng trong pack tăng lên,
tổng dung lượng thư mục .git giảm rõ rệt, đó là dấu hiệu bảo trì thành công. Lệnh
git fsck --full kiểm tra tính toàn vẹn của toàn bộ cơ sở dữ liệu đối tượng, nên chạy
sau mỗi lần can thiệp thủ công vào .git hoặc khi nghi ngờ kho bị hỏng.
Vậy khi nào cần bảo trì thủ công? Quy tắc thực tế gồm bốn trường hợp: sau khi viết
lại lịch sử bằng filter-repo hay rebase hàng loạt, trước khi sao lưu hoặc nhân bản kho
lớn, khi git status hay git fetch chậm bất thường, và định kỳ mỗi vài tháng với kho
đồ án có nhiều file nhị phân. Ngược lại, không nên lạm dụng git gc --aggressive hay
git prune vì thao tác này tốn CPU, viết lại toàn bộ packfile, và có thể xóa mất commit
mà reflog vẫn có thể cứu được nếu chạy với tùy chọn prune quá mạnh. Trên máy chạy CI
40

---

## [Page 42] (`page-42.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
như runner build project ASPX 4.8.1, thay vì gc thủ công, nên cấu hình fetch có cắt tỉa
và checkout nông để kho runner luôn gọn nhẹ [7].
Một lưu ý riêng cho project Web Forms: các thư mục Bin, packages và .vs sinh
ra hàng nghìn file nhị phân, nếu lỡ commit rồi mới thêm vào .gitignore thì lịch sử
vẫn giữ nguyên các blob nặng đó. Cách xử lý đúng là gỡ chúng khỏi chỉ mục bằng
git rm -r --cached, commit việc gỡ bỏ, rồi chạy git gc để đóng gói lại, dung lượng
kho sau đó thường giảm rất mạnh. Tóm lại, packfile giúp Git vừa toàn vẹn vừa gọn nhẹ,
còn git gc và git count-objects là hai công cụ chẩn đoán và bảo trì mà mọi thành
viên trong nhóm đồ án nên biết cách dùng [2].
Bốn chủ đề trên hợp thành bức tranh toàn cảnh về phần trong của Git: đối tượng và
hàm băm bảo đảm tính toàn vẹn, DAG cùng refs và HEAD tổ chức lịch sử thành đồ thị
linh hoạt, reflog là lưới an toàn cho sai lầm cá nhân, còn packfile và gc giữ cho kho luôn
gọn gàng. Nắm vững các cơ chế này, sinh viên không chỉ dùng Git thành thạo hơn mà
còn tự tin giải thích trong buổi bảo vệ vì sao Git phát hiện được mọi thay đổi dù nhỏ
nhất, vì sao nhánh lại nhẹ đến vậy, và vì sao commit tưởng mất vẫn có thể cứu lại. Trong
quy trình nhóm 3 người của đồ án ASPX, mỗi thành viên nên thực hành các khối lệnh
trong mục này trên kho DemoInternals của riêng mình trước khi áp dụng vào kho đồ án
chung.
3.5 Rebase và rebase tương tác
Khi mỗi thành viên làm trên một nhánh tính năng của project Web Forms, lệnh git rebase
giúp đặt lại toàn bộ nhánh lên đầu một nhánh mới hơn, tạo lịch sử thẳng và dễ đọc hơn
so với việc tạo thêm commit hợp nhất [2].
Về bản chất, rebase lấy từng commit trên nhánh hiện tại, tạm gỡ chúng ra, cập nhật
con trỏ lên đỉnh nhánh đích rồi áp dụng lại từng commit theo thứ tự, vì vậy mỗi commit
được viết lại với mã băm SHA mới [1].
Dạng mạnh nhất của rebase là rebase tương tác với cờ -i, cho phép biên tập lại cả
chuỗi commit trước khi áp dụng, ví dụ gộp nhiều commit thử nghiệm thành một commit
hoàn chỉnh trước khi mở pull request.
Khi chạy git rebase -i HEAD~3, Git mở một danh sách ba commit cùng hành động
đi kèm, trong đó bốn hành động dùng nhiều nhất là:
pick giữ nguyên commit, không thay đổi nội dung hay thông điệp.
reword giữ nguyên nội dung nhưng sửa lại nội dung thông điệp commit cho rõ nghĩa và
đúng chuẩn nhóm.
squash gộp commit này vào commit đứng ngay trước nó, đồng thời cho phép gộp cả hai
thông điệp thành một.
41

---

## [Page 43] (`page-43.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
drop loại bỏ commit khỏi lịch sử, thường dùng để xóa commit thử nghiệm hoặc commit
chưa từng được đẩy lên máy chủ.
Ví dụ sau gộp ba commit rời rạc khi dựng trang Default.aspx thành một commit
duy nhất có thông điệp đúng chuẩn Conventional Commits [3]:
1 git log -- oneline -3
2 # h7i8j9k them ghi chu tam vao form dang nhap
3 # e4f5g6h sua loi chinh ta tren nhan nut
4 # a1b2c3d tao trang Default . aspx ban dau
5 git rebase -i HEAD ~3
6 # Trong trinh soan thao , sua danh sach thanh :
7 # pick a1b2c3d tao trang Default . aspx ban dau
8 # squash e4f5g6h sua loi chinh ta tren nhan nut
9 # squash h7i8j9k them ghi chu tam vao form dang nhap
10 # Luu file , Git gop 3 commit va mo hop thoai nhap thong diep moi :
11 # feat : tao trang dang nhap Default . aspx
12 git log -- oneline -1
13 # k9l0m1n feat : tao trang dang nhap Default . aspx
Listing 13: Gop ba commit thanh mot commit bang rebase tuong tac
Nếu quá trình rebase gặp conflict, Git dừng lại ở commit đang áp dụng dở và chờ
người dùng xử lý; sau khi sửa file xong, chạy git add rồi git rebase --continue để đi
tiếp, hoặc git rebase --abort để hủy toàn bộ và quay về trạng thái ban đầu.
Cảnh báo quan trọng, nguyên tắc vàng của rebase: tuyệt đối không rebase các
commit đã đẩy lên nhánh công khai như main hay develop mà nhiều người đang dùng
chung.
Lý do là rebase viết lại mã băm SHA của mọi commit, nên đồng đội đã kéo bản cũ về
sẽ bị lệch lịch sử, phải xử lý conflict trùng lặp và có nguy cơ đẩy nhầm bản sao commit
lên máy chủ [2].
Quy tắc an toàn cho nhóm ba người: chỉ rebase nhánh tính năng của chính mình trước
khi mở pull request, và sau khi rebase nhánh riêng thì đẩy lên bằng git push --force-with-lease
thay vì đẩy ép buộc thông thường để tránh ghi đè nhầm công việc của người khác.
Trong đồ án ASPX, tình huống điển hình là nhánh feature/sua-giao-dien đã cũ hai
ngày so với develop; thành viên cập nhật nhánh của mình bằng git rebase develop
trên máy cá nhân, giải quyết mọi conflict ngay tại chỗ rồi mới mở pull request sạch sẽ.
3.6 So sánh merge, rebase và cherry-pick
Ba thao tác merge, rebase và cherry-pick đều dùng để kết hợp công việc giữa các
nhánh, nhưng mỗi thao tác tạo ra hình dạng lịch sử khác nhau và phù hợp với tình huống
khác nhau [1].
42

---

## [Page 44] (`page-44.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Lệnh merge giữ nguyên toàn bộ lịch sử hai phía rồi tạo thêm một commit hợp nhất,
nhờ đó phản ánh trung thực quá trình phát triển song song của nhóm.
Lệnh rebase viết lại chuỗi commit thành một đường thẳng gọn gàng nhưng thay đổi
mã băm SHA, vì vậy chỉ an toàn trên nhánh riêng như đã phân tích ở Mục 3.5.
Lệnh cherry-pick không hợp nhất cả nhánh mà chỉ chép đúng một commit sang vị
trí hiện tại, rất tiện cho việc mang bản vá nóng sang nhánh phát hành mà không kéo
theo các thay đổi dở dang khác.
Bảng 8 tổng hợp sáu tiêu chí quan trọng nhất để nhóm quyết định chọn thao tác nào
trong từng tình huống cụ thể.
Bảng 8: So sanh merge rebase va cherry pick theo sau tieu chi
Tiêu chí merge rebase cherry-pick
Lịch sử com￾mit
Giữ nguyên hai
phía, thêm một
commit hợp nhất
Viết lại thành một
đường thẳng gọn
gàng
Chỉ thêm đúng
một bản sao com￾mit
Mã băm SHA Không đổi với
commit cũ
Đổi toàn bộ com￾mit được viết lại
Bản sao mang
SHA mới
Xử lý conflict Giải một lần duy
nhất trong com￾mit hợp nhất
Có thể phải giải
lặp lại ở từng com￾mit
Giải một lần trên
bản sao duy nhất
Dùng khi nào Hợp nhất nhánh
tính năng đã re￾view xong
Làm sạch nhánh
riêng trước pull re￾quest
Mang bản vá nóng
sang nhánh khác
Ưu điểm chính Trung thực, an
toàn với nhánh
công khai
Lịch sử thẳng, dễ
đọc và dễ truy vết
Chính xác từng
commit, không
kéo việc dở dang
Rủi ro chính Nhiều commit hợp
nhất gây rối
Ghi đè lịch sử nếu
dùng sai nhánh
Dễ trùng lặp, khó
theo dõi nguồn
gốc
Quy ước gợi ý cho nhóm: dùng merge khi hợp nhất nhánh tính năng vào develop,
dùng rebase để cập nhật nhánh cá nhân trước khi xin review, và dùng cherry-pick khi
cần mang đúng một bản vá sang nhánh phát hành.
3.7 Cherry-pick và bản vá nóng
Trong đồ án Web Forms, tình huống kinh điển cần cherry-pick là khi phát hiện lỗi
nghiêm trọng trên nhánh main nhưng nhánh develop đang chứa nhiều tính năng dở dang
chưa thể phát hành.
43

---

## [Page 45] (`page-45.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Thay vì hợp nhất cả hai nhánh, trưởng nhóm sửa lỗi trực tiếp trên main, tạo một
commit vá nóng rồi dùng cherry-pick để chép đúng commit đó sang develop, đảm bảo
bản phát hành tiếp theo cũng hết lỗi [2].
Cú pháp cơ bản chỉ gồm mã băm của commit cần chép, ngoài ra cờ -x còn tự động
ghi thêm một dòng chú thích nguồn gốc vào thông điệp để sau này dễ truy vết.
Ví dụ đầy đủ dưới đây vá lỗi chuỗi kết nối trong Web.config trên main rồi mang đúng
bản vá sang develop:
1 git checkout main
2 # Sua truc tiep loi chuoi ket noi trong Web . config roi commit :
3 git add Web . config
4 git commit -m " fix : sua chuoi ket noi SQL Server tren main "
5 git log -- oneline -1
6 # p1q2r3s fix : sua chuoi ket noi SQL Server tren main
7 git checkout develop
8 git cherry - pick -x p1q2r3s
9 # Git tao mot ban sao commit tren develop , kem dong ghi nguon goc
:
10 # ( cherry picked from commit p1q2r3s ...)
11 git log -- oneline -1
12 # t4u5v6w fix : sua chuoi ket noi SQL Server tren main
Listing 14: Chep mot commit va nong tu main sang develop
Nếu bản vá conflict với code trên develop, Git dừng lại và đánh dấu file lỗi giống
như khi hợp nhất; sau khi sửa xong, chạy git add rồi git cherry-pick --continue để
hoàn tất, hoặc git cherry-pick --abort để hủy bỏ.
Cần lưu ý rằng bản sao do cherry-pick tạo ra mang mã băm SHA khác commit gốc,
vì vậy không nên lạm dụng cho hàng loạt commit, trường hợp đó nên dùng merge hoặc
rebase để lịch sử rõ ràng hơn.
Sau khi chép xong, nhóm nên chạy lại toàn bộ solution ASPX trên máy cá nhân rồi
mới đẩy lên máy chủ, tránh mang lỗi biên dịch từ nhánh này sang nhánh khác.
3.8 Git bisect truy tìm commit gây lỗi
Khi hệ thống ASPX bỗng dưng đổ vỡ mà không ai nhớ thay đổi nào gây ra, lệnh
git bisect sẽ tìm giúp commit thủ phạm bằng chiến lược tìm kiếm nhị phân, mỗi
bước loại bỏ một nửa số commit nghi vấn [2].
Toàn bộ quy trình gồm sáu bước, lặp đi lặp lại cho đến khi Git chỉ còn đúng một
commit khả nghi:
1. Chuẩn bị một cách kiểm lỗi nhanh và lặp lại được, ví dụ biên dịch solution bằng
msbuild hoặc mở trang Default.aspx để xem lỗi còn tái hiện hay không.
44

---

## [Page 46] (`page-46.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
2. Khởi động phiên tìm kiếm bằng git bisect start để Git ghi nhớ điểm xuất phát.
3. Đánh dấu commit hiện tại đang lỗi bằng git bisect bad.
4. Đánh dấu một commit cũ chắc chắn còn tốt bằng git bisect good, ví dụ thẻ phiên
bản phát hành trước đó.
5. Kiểm tra commit ở giữa mà Git tự động chọn, rồi đánh dấu git bisect good hoặc
git bisect bad; lặp lại bước này cho đến khi Git báo đã tìm thấy commit gây lỗi
đầu tiên.
6. Ghi nhận kết quả, kết thúc phiên bằng git bisect reset để quay về nhánh ban
đầu, rồi tiến hành sửa lỗi.
Ví dụ sau minh họa đầy đủ một phiên tìm lỗi trong project Web Forms có mười
commit gần nhất:
1 git bisect start
2 git bisect bad HEAD
3 git bisect good v1 .0
4 # Git checkout commit o giua , vi du f6g7h8i , ta kiem thu :
5 msbuild AspxDemo . sln / p : Configuration = Release
6 # Bien dich loi , trang Default . aspx trang tinh , danh dau xau :
7 git bisect bad
8 # Git thu hep pham vi , checkout commit tiep theo de kiem tra :
9 msbuild AspxDemo . sln / p : Configuration = Release
10 # Lan nay bien dich tot , trang hien thi binh thuong :
11 git bisect good
12 # Lap lai vai vong , cuoi cung Git bao :
13 # d3e4f5g is the first bad commit
14 git bisect reset
15 # Ve nhanh ban dau , bat dau doc commit d3e4f5g de sua loi
Listing 15: Quy trinh git bisect tim commit gay loi dau tien
Với project lớn có hàng trăm commit, có thể tự động hóa bước kiểm tra bằng git bisect run,
ví dụ git bisect run msbuild AspxDemo.sln để Git tự chạy lệnh sau mỗi lần chuyển
commit và tự kết luận tốt hay xấu theo mã thoát.
Hình 6 tóm tắt vòng lặp thu hẹp phạm vi của git bisect từ khoảng nghi vấn ban
đầu đến commit gây lỗi đầu tiên.
Chon khoang Thu commit giua Danh gia tot xau Tim commit loi
bisect kiem tra thu hep
Hình 6: Vong lap thu hep pham vi cua git bisect
45

---

## [Page 47] (`page-47.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Sau khi tìm ra commit thủ phạm, nhóm nên đọc kỹ thay đổi bằng git show rồi quyết
định sửa tiếp bằng commit mới hay hoàn tác bằng git revert, tuyệt đối không xóa lịch
sử đã công khai.
3.9 Rerere và worktree
Hai tính năng rerere và worktree ít được nhắc tới nhưng lại tiết kiệm rất nhiều thời
gian cho nhóm sinh viên khi conflict lặp đi lặp lại hoặc khi cần làm nhiều nhánh cùng lúc
[2].
3.9.1 Cơ chế ghi nhớ cách giải conflict của rerere
Tên rerere là viết tắt của cụm từ tiếng Anh reuse recorded resolution, nghĩa là tái sử
dụng cách giải conflict đã ghi nhớ; sau khi bật, Git tự lưu lại hình ảnh trước và sau mỗi
lần người dùng giải conflict thành công.
Những lần sau gặp đúng mẫu conflict đó, Git tự áp dụng lại cách giải cũ và chỉ thông
báo để người dùng kiểm tra, thay vì bắt giải lại từ đầu; cơ chế này đặc biệt hữu ích khi
rebase dài ngày hoặc hợp nhất nhánh release lặp đi lặp lại.
Cách bật và kiểm tra rerere trên máy cá nhân gồm hai lệnh đơn giản, trong đó cờ
--global áp dụng cho mọi repo của người dùng:
1 git config -- global rerere . enabled true
2 git config -- global rerere . autoupdate true
3 # Tu bay gio , moi lan giai conflict xong , Git tu ghi nho cach
giai
4 # Kiem tra cac mau conflict da luu trong repo hien tai :
5 git rerere status
6 git rerere diff
Listing 16: Bat rerere va kiem tra thu muc ghi nho
Trong đồ án ASPX, mẫu conflict lặp lại nhiều nhất nằm ở file Web.config khi mỗi
thành viên thêm một đoạn cấu hình khác nhau; nhờ rerere, từ lần thứ hai trở đi Git tự
gộp lại đúng như lần đầu và nhóm chỉ cần mở file kiểm tra rồi commit.
3.9.2 Làm nhiều nhánh cùng lúc với worktree
Mặc định mỗi thư mục chỉ checkout được một nhánh tại một thời điểm, nhưng lệnh
git worktree cho phép tạo thêm các thư mục liên kết, mỗi thư mục giữ một nhánh khác
nhau mà vẫn dùng chung một kho .git duy nhất.
Nhờ đó sinh viên có thể vừa chạy thử nhánh release/v1.0 trên máy chủ IIS Express
ở thư mục chính, vừa phát triển tiếp nhánh feature/thanh-toan ở thư mục bên cạnh
mà không cần đóng mở hay cất tạm công việc [1].
46

---

## [Page 48] (`page-48.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Ví dụ sau tạo một worktree mới cho nhánh tính năng, liệt kê toàn bộ worktree rồi dọn
dẹp khi làm xong:
1 git worktree add ../ aspx - hotfix feature / thanh - toan
2 # Thu muc ../ aspx - hotfix nay checkout nhanh feature / thanh - toan
3 git worktree list
4 # D :/ TuHoc_ASPX ab12cd3 [ main ]
5 # D :/ TuHoc_ASPX - hotfix ef45gh6 [ feature / thanh - toan ]
6 cd ../ aspx - hotfix
7 msbuild AspxDemo . sln / p : Configuration = Release
8 cd ../ TuHoc_ASPX
9 git worktree remove ../ aspx - hotfix
Listing 17: Tao liet ke va don dep worktree
Cần nhớ hai giới hạn: mỗi nhánh chỉ được checkout ở đúng một worktree tại một thời
điểm, và không nên xóa thư mục worktree bằng tay mà hãy dùng git worktree remove
để Git dọn dẹp cả siêu dữ liệu liên quan.
Kết hợp cả hai công cụ, quy trình nhóm trở nên gọn gàng: bật rerere một lần rồi
quên đi, dùng worktree khi cần song song hai nhánh, dùng rebase cho nhánh riêng, merge
cho nhánh chung và cherry-pick cho bản vá nóng.
3.10 Git hooks: kiểm soát tự động với pre-commit, commit-msg
và pre-push
Git hooks là các script mà Git tự động thực thi khi một sự kiện xảy ra, ví dụ trước khi
tạo commit, trước khi đẩy code lên máy chủ hay sau khi hợp nhất nhánh. Mỗi repo đều
có thư mục mẫu .git/hooks chứa các file ví dụ kết thúc bằng .sample; muốn kích hoạt
hook nào thì đổi tên bỏ đuôi .sample và cấp quyền thực thi cho file đó [2].
Ba hooks hữu ích nhất cho nhóm làm đồ án ASPX được tóm tắt như sau:
• pre-commit: chạy trước khi Git tạo commit. Dùng để chặn commit chứa chuỗi cấm,
chặn file quá lớn hoặc yêu cầu định dạng code thống nhất.
• commit-msg: chạy sau khi lập trình viên nhập thông điệp commit. Dùng để kiểm
tra thông điệp có đúng định dạng đã thống nhất hay không.
• pre-push: chạy trước khi Git đẩy commit lên máy chủ. Dùng để chạy kiểm tra cuối,
ví dụ cấm push trực tiếp lên nhánh main hoặc cấm push khi còn lỗi biên dịch.
Ví dụ thực tế: nhóm quy định không ai được commit chuỗi connStrThat vì đây là
dấu hiệu lập trình viên đã dán nhầm chuỗi kết nối thật vào mã nguồn. Script pre-commit
dưới đây quét toàn bộ nội dung chuẩn bị commit và chặn lại khi phát hiện chuỗi cấm:
47

---

## [Page 49] (`page-49.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
1 # !/ bin / sh
2 # Block commit when staged content contains connStrThat
3 if git diff -- cached | grep -q " connStrThat " ; then
4 echo " ERROR : found connStrThat in staged changes . "
5 echo " Remove the real connection string and use Web . config .
transform instead . "
6 exit 1
7 fi
8 exit 0
Listing 18: Hook pre-commit chan commit chua chuoi cam
Để kích hoạt, lưu file trên thành .git/hooks/pre-commit rồi chạy chmod +x .git/hooks/pre-commit
trên Git Bash. Từ lúc đó, mỗi lần gõ git commit, Git sẽ chạy script trước; nếu script trả
về mã lỗi khác không thì commit bị hủy và lập trình viên phải sửa code rồi commit lại.
Cách làm này rẻ, chạy ngay trên máy cá nhân và ngăn lỗi lộ thông tin nhạy cảm từ rất
sớm [1].
Cần lưu ý hooks trong thư mục .git/hooks không được Git theo dõi nên không tự
lan sang máy của thành viên khác khi clone. Nhóm nên lưu bản chuẩn của hooks vào thư
mục tools/hooks trong repo rồi thêm bước sao chép vào tài liệu hướng dẫn cài đặt, hoặc
dùng biến cấu hình core.hooksPath để trỏ mọi máy về cùng một thư mục hooks dùng
chung.
3.11 Git LFS: quản lý file lớn như video, bộ cài đặt và thư viện
dll
Git lưu toàn bộ lịch sử dưới dạng các đối tượng nén, vì vậy các file nhị phân lớn như
video demo, bộ cài đặt hay thư viện dll của bên thứ ba sẽ làm repo phình to rất nhanh
và mỗi lần clone đều phải tải lại toàn bộ các phiên bản cũ. Git LFS (Large File Storage)
giải quyết vấn đề này bằng cách thay nội dung file lớn trong repo bằng một con trỏ văn
bản nhỏ, còn nội dung thật được lưu trên máy chủ LFS [2].
Ba lệnh cơ bản đủ để nhóm bắt đầu với LFS như sau:
1. Cài đặt và kích hoạt LFS một lần trên mỗi máy với git lfs install.
2. Khai báo mẫu file cần theo dõi, ví dụ git lfs track "*.mp4" cho video demo và
git lfs track "*.dll" cho thư viện ngoài, rồi commit file .gitattributes sinh
ra.
3. Thêm, commit và push như bình thường; các lệnh git add, git commit và git push
vẫn giữ nguyên, LFS tự động tải nội dung lớn lên máy chủ.
48

---

## [Page 50] (`page-50.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
1 # One - time setup on each machine
2 git lfs install
3 # Track large files , then commit the . gitattributes file
4 git lfs track " *. mp4 "
5 git lfs track " *. dll "
6 git add . gitattributes
7 git commit -m " chore : track large media with LFS "
8 # Use add , commit and push as usual
9 git add Demo_Video . mp4 ThirdParty . dll
10 git commit -m " docs : add demo video and vendor lib "
11 git push origin main
Listing 19: Ba lenh Git LFS co ban cho file lon
Với project ASPX, quy tắc thực tế là chỉ đưa vào LFS các file bắt buộc phải ở trong
repo như video demo hay thư viện không có trên NuGet; các gói khôi phục được bằng
NuGet và thư mục bin hay obj phải cho vào .gitignore thay vì LFS. Cả GitHub và
GitLab đều hỗ trợ LFS nhưng giới hạn băng thông và dung lượng miễn phí, vì vậy nhóm
sinh viên nên giữ số lượng file LFS ở mức tối thiểu [6, 8].
3.12 Submodule và subtree: tái sử dụng mã nguồn giữa các repo
Khi đồ án ASPX cần dùng chung một thư viện, ví dụ bộ kiểm tra dữ liệu hay bộ giao diện
dùng cho nhiều project, nhóm có hai cách chính để tái sử dụng mà không sao chép thủ
công: submodule và subtree. Submodule nhúng một repo khác vào thư mục con và ghi lại
đúng mã commit đang dùng; subtree hợp nhất lịch sử của repo khác vào repo chính như
một thư mục bình thường [2].
Bảng 9: So sanh submodule va subtree
Tiêu chí Submodule Subtree
Lịch sử Nằm ở repo riêng, repo chính chỉ giữ con trỏ Gộp chung vào lịch sử repo chính
Lệnh clone Cần thêm --recurse-submodules Clone bình thường, không cần cờ đặc biệt
Cập nhật Hai bước: kéo repo con rồi commit con trỏ mới Một bước: kéo và hợp nhất như thư mục thường
Đẩy sửa lên thư viện Commit trong thư mục con rồi push riêng Tách và đẩy bằng lệnh subtree push
Độ phức tạp Cao hơn, dễ quên cập nhật con trỏ Thấp hơn, thân thiện với người mới
Khuyến nghị cho nhóm ba người: dùng subtree khi thư viện do chính nhóm sở hữu và
ít tách ra phát triển độc lập, vì mọi thành viên chỉ cần học các lệnh Git thông thường.
Chỉ dùng submodule khi thư viện là repo ngoài do nhóm khác bảo trì và cần ghim đúng
một phiên bản đã kiểm thử, ví dụ ghim đúng commit đã chạy ổn định của bộ điều khiển
49

---

## [Page 51] (`page-51.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
dùng chung. Trong cả hai trường hợp, nhóm đều phải ghi rõ trong tài liệu hướng dẫn câu
lệnh clone và cập nhật để thành viên mới không bị thiếu code [1].
3.13 Ký commit bằng GPG và SSH: chống giả mạo tác giả
Mặc định Git tin hoàn toàn tên và email do người dùng khai báo, vì vậy bất kỳ ai cũng
có thể giả tên người khác khi tạo commit. Ký commit (commit signing) gắn một chữ ký
số vào mỗi commit để máy chủ xác thực đúng tác giả; trên GitHub và GitLab, commit
đã xác thực sẽ hiện nhãn Verified rất tin cậy khi chấm bài [6, 8].
Bốn lệnh cấu hình đủ cho sinh viên bắt đầu ký bằng khóa SSH đã có như sau. Nhóm
dùng khóa SSH vì đơn giản hơn GPG mà vẫn được cả hai nền tảng chấp nhận:
1 # 1. Create an SSH signing key ( skip if you already have one )
2 ssh - keygen -t ed25519 -C " sv03@example . com " -f ~/. ssh / id_sign
3 # 2. Tell Git to sign with SSH and use your key
4 git config -- global gpg . format ssh
5 git config -- global user . signingkey ~/. ssh / id_sign . pub
6 # 3. Sign every commit automatically
7 git config -- global commit . gpgsign true
8 # 4. Show signatures in the log to verify
9 git log -- show - signature -n 3
Listing 20: Cau hinh ky commit bang khoa SSH
Sau khi cấu hình, mỗi lần chạy git commit thì Git sẽ ký tự động; nếu muốn ký thủ
công từng commit thì thêm cờ -S như git commit -S -m "feat: them kiem tra" .
Bước còn lại là dán nội dung file id_sign.pub vào mục SSH and GPG keys trên GitHub
và mục SSH Keys trên GitLab để máy chủ nhận diện chữ ký. Với đồ án môn học, nhóm
nên yêu cầu ít nhất nhánh main chỉ nhận commit đã ký, vừa chống giả mạo vừa tạo thói
quen bảo mật tốt [2].
3.14 Sparse-checkout và partial clone cho repo khổng lồ
Một số repo môn học hoặc repo công ty chứa hàng nghìn thư mục nhưng mỗi sinh viên
chỉ làm trên một phần nhỏ, ví dụ chỉ thư mục BaoCao_LaTeX hoặc chỉ project AspxDemo.
Tải toàn bộ cây thư mục vừa chậm vừa tốn ổ cứng. Sparse-checkout cho phép chỉ lấy ra
(check out) một số thư mục cần thiết, còn partial clone cho phép tải trước khung lịch sử
rồi tải nội dung file khi thật sự cần [2].
Quy trình gọn nhất gồm ba bước: clone với bộ lọc để bỏ nội dung file lớn, bật sparse￾checkout ở chế độ hình nón rồi liệt kê các thư mục muốn giữ lại. Ví dụ dưới đây chỉ lấy
báo cáo và slide, bỏ qua toàn bộ video demo:
1 # 1. Clone without file contents , download on demand
50

---

## [Page 52] (`page-52.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
2 git clone -- filter = blob : none --no - checkout https :// github . com / lop
/ aspx - group . git
3 cd aspx - group
4 # 2. Enable cone - mode sparse checkout
5 git sparse - checkout init -- cone
6 # 3. Keep only the report and slide folders
7 git sparse - checkout set BaoCao_LaTeX Slide_LaTeX
8 git checkout main
9 # Later , add one more folder when needed
10 git sparse - checkout add AspxDemo
Listing 21: Clone loc va giu hai thu muc can thiet
Khi cần quay lại đầy đủ repo, chạy git sparse-checkout disable rồi git checkout
để khôi phục toàn bộ cây thư mục. Lưu ý sparse-checkout chỉ ẩn file khỏi thư mục làm
việc chứ không xóa lịch sử trên máy chủ, vì vậy các lệnh git log và git diff vẫn thấy
đầy đủ thông tin. Với máy cấu hình yếu hoặc mạng ký túc xá chậm, đây là kỹ thuật tiết
kiệm thời gian rõ rệt nhất khi làm việc với repo lớn [1].
3.15 Viết lại lịch sử an toàn với filter-repo khi lộ connection
string
Tình huống kinh điển của nhóm ASPX: một thành viên vô tình commit file Web.config
chứa chuỗi kết nối thật có tên máy chủ và mật khẩu, rồi push lên repo chung. Xóa file
ở commit mới không đủ vì chuỗi nhạy cảm vẫn nằm trong lịch sử cũ và bất kỳ ai cũng
xem lại được. Công cụ khuyên dùng hiện nay là git filter-repo, nhanh và an toàn hơn
lệnh filter-branch đã lỗi thời [2].
Quy trình xử lý gồm bốn bước: thông báo cho cả nhóm dừng push, sao lưu repo, chạy
filter-repo để thay chuỗi nhạy cảm trong toàn bộ lịch sử, rồi push đè có kiểm soát và xoay
lại mật khẩu ngay. Ví dụ dưới đây thay chuỗi connStrThat bằng văn bản giữ chỗ trong
mọi commit:
1 # 0. Backup first , history rewrite is destructive
2 git clone -- mirror https :// github . com / lop / aspx - group . git backup .
git
3 # 1. Install filter - repo once ( Windows example with pip )
4 pip install git - filter - repo
5 # 2. Replace the leaked secret in every commit
6 git filter - repo -- replace - text <( echo " connStrThat == >
REMOVED_SECRET " )
7 # 3. Reconnect the remote and force - push with lease
8 git remote add origin https :// github . com / lop / aspx - group . git
51

---

## [Page 53] (`page-53.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
9 git push -- force - with - lease origin main
Listing 22: Xoa chuoi ket noi that khoi toan bo lich su
Cảnh báo quan trọng: viết lại lịch sử đổi toàn bộ mã định danh commit nên mọi thành
viên phải xóa bản cũ và clone lại, tuyệt đối không hợp nhất bản cũ vào bản mới. Luôn
dùng --force-with-lease thay vì --force để Git từ chối push đè khi có người vừa đẩy
commit mới mà mình chưa thấy. Sau khi push đè, nhóm phải đổi mật khẩu cơ sở dữ liệu
và chuỗi kết nối ngay vì bí mật đã lộ không thể coi là an toàn nữa, đồng thời chuyển sang
dùng biến môi trường và kho secret của pipeline [6, 8].
3.16 Quy trình nhánh: GitFlow, GitHub Flow và Trunk-Based
Development
Quy trình nhánh quy định code đi từ máy cá nhân lên nhánh chính bằng con đường nào
và kiểm soát chất lượng ở đâu. Ba mô hình phổ biến nhất là GitFlow với nhiều nhánh dài
hạn, GitHub Flow gọn nhẹ xoay quanh nhánh chính và pull request, cùng Trunk-Based
Development nơi mọi người tích hợp trực tiếp vào thân chính mỗi ngày [4].
Bảng 10: So sanh ba quy trinh nhanh pho bien
Tiêu chí GitFlow GitHub Flow Trunk-Based
Nhánh dài hạn main và develop Chỉ main Chỉ main hoặc trunk
Nhánh tính năng Có, hợp nhất vào develop Có, hợp nhất vào main Ngắn, tồn tại dưới một ngày
Phát hành Nhánh release riêng Thẻ và triển khai liên tục Triển khai liên tục, cờ tính năng
Mức phức tạp Cao, nhiều quy tắc Thấp, dễ học Trung bình, cần kỷ luật cao
Phù hợp Sản phẩm có phiên bản Nhóm nhỏ, web, đồ án Nhóm lớn, triển khai mỗi ngày
Hình dưới đây minh họa luồng GitHub Flow mà nhóm ba người nên dùng: mỗi tính
năng là một nhánh ngắn tách từ main, hoàn thành thì mở pull request để một bạn review,
pipeline chạy xanh mới được hợp nhất trở lại main.
Nhanh main Nhanh tinh nang Pull request tach nhanh mo review
merge khi xanh
Hình 7: Luong GitHub Flow cho nhom ba sinh vien
Khuyến nghị chốt cho nhóm ba người làm đồ án ASPX: chọn GitHub Flow vì chỉ có
một nhánh dài hạn nên ít nhầm lẫn, mỗi pull request là một bằng chứng review để đưa
vào báo cáo, và pipeline kiểm tra tự động ngay trên pull request. GitFlow chỉ nên dùng khi
đồ án yêu cầu quản lý nhiều phiên bản phát hành song song; Trunk-Based Development
52

---

## [Page 54] (`page-54.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
tuy hiện đại nhưng đòi hỏi kiểm thử tự động rất mạnh và thói quen commit mỗi ngày mà
sinh viên khó duy trì [4, 1].
3.17 Conventional Commits: chuẩn hóa thông điệp commit cho
cả nhóm
Khi ba người cùng commit vào một repo, thông điệp tùy hứng như đã sửa hay cập
nhật code khiến lịch sử không thể đọc được và giảng viên khó chấm điểm đóng góp.
Conventional Commits quy định một định dạng thống nhất type(scope): subject gồm
loại thay đổi, phạm vi tác động trong ngoặc đơn và mô tả ngắn ở thì hiện tại [3].
Các loại phổ biến gồm feat cho tính năng mới, fix cho sửa lỗi, docs cho tài liệu,
style cho định dạng không đổi logic, refactor cho tái cấu trúc, test cho kiểm thử và
chore cho việc vặt như cập nhật công cụ. Phần scope nêu rõ module chịu ảnh hưởng, ví
dụ auth cho đăng nhập hay aspx cho trang Web Forms, giúp chỉ đọc một dòng log cũng
biết commit chạm vào đâu.
Sáu ví dụ đúng chuẩn gắn với đồ án ASPX của nhóm như sau:
1 # New feature , bug fix , docs , refactor , test , chores
2 git commit -m " feat ( auth ) : add login check for admin page "
3 git commit -m " fix ( aspx ) : correct Web . config transform path "
4 git commit -m " docs ( report ) : describe Git LFS for demo video "
5 git commit -m " refactor ( cart ) : split checkout into small methods "
6 git commit -m " test ( login ) : add cases for wrong password "
7 git commit -m " chore ( ci ) : cache NuGet packages in pipeline "
Listing 23: Sau thong diep commit dung chuan
Để ép cả nhóm tuân thủ, kết hợp ba biện pháp: mẫu commit-msg hook kiểm tra định
dạng ngay trên máy cá nhân, pipeline kiểm tra tên commit trong mỗi pull request, và
quy ước người review từ chối các pull request có thông điệp sai chuẩn. Lợi ích thu được
rất thiết thực: lệnh git log --oneline trở thành nhật ký công việc rõ ràng, công cụ tự
động sinh ghi chú phát hành từ tiền tố loại commit, và giảng viên chỉ cần đọc lịch sử
cũng đánh giá được ai làm phần nào [3, 2].
Tóm lại, tám kỹ thuật trong mục này tạo thành bộ công cụ nâng cao cho nhóm: hooks
và ký commit bảo vệ chất lượng từ máy cá nhân, LFS cùng sparse-checkout xử lý repo
lớn, submodule và filter-repo quản lý mã dùng chung và sự cố lộ bí mật, còn quy trình
nhánh và Conventional Commits giữ cho ba người phối hợp nhịp nhàng đến ngày nộp
bài.
53

---

## [Page 55] (`page-55.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
4 GitHub
GitHub là nền tảng cộng tác dựa trên Git được dùng phổ biến nhất hiện nay cho đồ án
môn học và dự án phần mềm. Nếu Git quản lý lịch sử thay đổi trên máy cá nhân thì
GitHub cung cấp kho chứa tập trung, công cụ trao đổi và quy trình kiểm soát chất lượng.
Chương này trình bày các thành phần cốt lõi của GitHub và gắn trực tiếp với đồ án
ASPX trên .NET Framework 4.8.1. Sinh viên đọc xong có thể tạo kho chứa, mở Issues,
làm việc với Fork và Pull Request, đánh giá code và thiết lập bảo vệ nhánh.
4.1 Tổng quan: Git là công cụ, GitHub là nền tảng cộng tác
Git là hệ thống quản lý phiên bản phân tán, mỗi máy đều giữ đầy đủ lịch sử commit,
nhánh và thẻ. GitHub là dịch vụ trực tuyến xây dựng quanh Git, bổ sung giao diện web,
quản lý quyền truy cập, thảo luận và tự động hóa [6]. Cách phân biệt ngắn gọn là Git
theo dõi thay đổi còn GitHub giúp con người phối hợp xoay quanh các thay đổi đó [2].
Một nhóm đồ án ASPX thường dùng Git để commit code trên máy cá nhân và dùng
GitHub để đồng bộ, phân công và kiểm tra chéo.
GitHub tổ chức công việc theo kho chứa, mỗi kho chứa gom toàn bộ mã nguồn, tài
liệu, lịch sử và thiết lập của một dự án. Xung quanh kho chứa là các công cụ cộng tác
như Issues, Pull Request, Projects, Wiki và Discussions. Quy trình chuẩn của nhóm nhỏ
là mọi thay đổi đều đi qua Pull Request, có ít nhất một người khác đọc lại trước khi hợp
nhất. Cách làm này giúp lỗi cú pháp, lỗi logic và cấu hình sai được phát hiện sớm thay
vì dồn đến ngày nộp bài.
Đối với đồ án Web Forms trên .NET Framework 4.8.1, GitHub còn là nơi lưu trữ minh
chứng làm việc nhóm. Lịch sử commit cho thấy ai đã làm phần nào, Pull Request ghi
lại trao đổi và quyết định kỹ thuật. Giảng viên có thể mở biểu đồ đóng góp, danh sách
commit và các Pull Request đã hợp nhất để đánh giá quá trình. Vì vậy nhóm nên commit
thường xuyên với thông điệp rõ ràng theo Conventional Commits [3] thay vì dồn một
commit lớn cuối kỳ.
Các thao tác Git cơ bản vẫn thực hiện dưới dòng lệnh rồi đồng bộ lên GitHub. Lệnh
git clone tải kho chứa về máy, git pull cập nhật thay đổi mới và git push gửi commit
lên máy chủ. Nhánh được tạo bằng git checkout -b hoặc git switch -c, sau đó gửi
lên GitHub để mở Pull Request. Tài liệu chính thức của GitHub mô tả đầy đủ vòng đời
này từ tạo kho chứa đến hợp nhất và triển khai [6].
Một kho chứa đồ án ASPX nên có cấu trúc gọn gàng ngay từ đầu để việc cộng tác
thuận lợi. Thư mục gốc giữ file giải pháp, thư mục dự án giữ các trang Login.aspx và
Default.aspx. File Web.config giữ cấu hình chung, thư mục App-Data hoặc App-Code
giữ dữ liệu và mã dùng chung. File README.md mô tả cách mở dự án bằng Visual Studio,
cách biên dịch bằng msbuild và cách chạy thử. Nhóm cũng nên thêm file .gitignore
chuẩn cho Visual Studio để không đưa thư mục bin, obj và packages lên GitHub.
54

---

## [Page 56] (`page-56.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
4.2 Kho chứa, Issues, Projects, Wiki và Discussions
Repository là đơn vị trung tâm trên GitHub, chứa mã nguồn, lịch sử commit, nhánh, thẻ
và toàn bộ thiết lập cộng tác. Mỗi repository có địa chỉ web riêng, trang tổng quan hiển
thị cây thư mục, file giới thiệu và trạng thái nhánh mặc định. Với đồ án ASPX, nhóm
đặt tên kho chứa rõ ràng như AspxDemo-NET481 và viết phần mô tả nêu đúng phiên bản
Framework. Nhóm bật Issues và Discussions ngay khi tạo kho chứa để mọi trao đổi đều
lưu lại một chỗ thay vì nhắn tin rời rạc.
Issues là nơi ghi nhận công việc, lỗi và ý tưởng cải tiến dưới dạng các thẻ có thể gán
người thực hiện và nhãn. Mỗi Issue có tiêu đề, mô tả, bình luận, nhãn, mốc thời gian
và trạng thái đóng hoặc mở. Ví dụ gắn với đồ án là Issue tiêu đề đăng nhập báo lỗi khi
bỏ trống mật khẩu, nhãn lỗi, gán cho thành viên phụ trách trang đăng nhập. Khi Pull
Request sửa xong vấn đề, thông điệp commit ghi câu đóng Issue tự động để lịch sử được
liên kết chặt chẽ.
Projects là bảng quản lý công việc dạng kanban với các cột việc cần làm, đang làm
và đã xong. Mỗi thẻ trên bảng có thể liên kết tới một hoặc nhiều Issue và Pull Request
tương ứng. Ví dụ nhóm ASPX lập bảng gồm các cột ý tưởng, đang phát triển, chờ đánh
giá và đã hoàn thành. Đầu tuần nhóm kéo các Issue như viết trang đăng nhập, viết trang
quản trị và sửa file cấu hình vào cột phù hợp. Cuối tuần giảng viên mở bảng là thấy ngay
tiến độ mà không cần hỏi từng thành viên.
Wiki là hệ thống trang tài liệu riêng của kho chứa, phù hợp cho hướng dẫn dài và ít
thay đổi theo từng commit. Nhóm có thể viết các trang như hướng dẫn cài đặt, hướng
dẫn cấu hình máy chủ và quy ước đặt tên cho các trang Web Forms. Ví dụ trang hướng
dẫn biên dịch ghi rõ mở Visual Studio phiên bản nào, chọn cấu hình Release và chạy lệnh
biên dịch ra sao. Trang hướng dẫn cấu hình ghi rõ các khóa trong file Web.config mà
không ghi giá trị mật khẩu thật. Nhờ Wiki, thành viên mới vào nhóm chỉ cần đọc vài
trang là chạy được dự án mà không phải hỏi lại từ đầu.
Discussions là diễn đàn thảo luận mở cho các câu hỏi, ý tưởng và thông báo không
phải là lỗi cụ thể. Khác với Issues vốn dùng để theo dõi việc cần đóng, Discussions phù
hợp cho trao đổi như nên dùng Master Page nào cho phần quản trị. Ví dụ nhóm mở một
thảo luận về cách tổ chức thư mục cho trang quản trị, mỗi người nêu một phương án rồi
bỏ phiếu. Sau khi thống nhất, nhóm tạo Issue triển khai phương án đã chọn và đóng thảo
luận bằng một bản tóm tắt. Cách tách bạch này giữ cho danh sách Issues luôn gọn và chỉ
chứa việc có thể hoàn thành được.
Năm công cụ trên tạo thành một vòng khép kín cho đồ án môn học từ ý tưởng đến
tài liệu. Thảo luận thống nhất ý tưởng, Issues chia việc, Projects theo dõi tiến độ, Pull
Request hợp nhất code và Wiki lưu kiến thức lâu dài. Nhóm ba sinh viên nên thống nhất
ngay tuần đầu ai tạo kho chứa, ai quản lý bảng Projects và ai viết trang Wiki đầu tiên.
Mọi quyết định quan trọng như đổi tên nhánh chính hay đổi cấu trúc thư mục đều nên ghi
55

---

## [Page 57] (`page-57.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
lại trong Issues hoặc Discussions. Nhờ vậy báo cáo cuối kỳ có thể trích dẫn đúng đường
dẫn Issue và Pull Request làm minh chứng làm việc nhóm.
4.3 Fork và Pull Request
Fork là bản sao độc lập của một kho chứa nằm dưới tài khoản của người sao chép. Branch
là nhánh nằm trong cùng một kho chứa, dùng chung Issues, Projects và thiết lập bảo vệ.
Bảng sau đây tóm tắt khi nào nên dùng Fork và khi nào nên dùng Branch cho đồ án môn
học.
Tiêu chí Fork Branch
Phạm vi Kho chứa mới dưới tài khoản riêng Nhánh mới trong cùng kho chứa
Quyền cần có Không cần quyền ghi kho gốc Cần quyền ghi hoặc quyền tạo nhánh
Đối tượng Người ngoài tổ chức đóng góp Thành viên trong nhóm đồ án
Quản lý Chủ fork tự quản lý bản sao Nhóm quản lý tập trung một chỗ
Đồng bộ Phải kéo thủ công từ kho gốc Tự thấy nhánh mới sau khi đẩy lên
Phù hợp ASPX Sinh viên khác sửa lỗi giúp Ba thành viên làm tính năng mỗi tuần
Dọn dẹp Xóa fork khi không dùng nữa Xóa nhánh sau khi hợp nhất
Bảng 11: Fork va branch khi nao dung trong do an ASPX
Với nhóm ba sinh viên cùng làm một đồ án, Branch kết hợp Pull Request là lựa chọn
gọn nhất. Mỗi tính năng như trang đăng nhập hay trang quản trị được làm trên một
nhánh riêng rồi hợp nhất qua Pull Request. Fork chỉ nên dùng khi muốn thử nghiệm độc
lập hoặc khi người ngoài nhóm muốn gửi bản sửa mà không có quyền ghi. Câu hỏi Fork
khác Branch khi nào là một trong các câu phản biện quen thuộc của phần GitHub [1].
Nhóm nên trả lời ngắn gọn là trong nhóm dùng Branch, ngoài nhóm dùng Fork.
Vòng đời Pull Request chuẩn gồm năm bước là đẩy nhánh, mở Pull Request, đánh giá,
kiểm tra tự động và hợp nhất. Bước một, lập trình viên đẩy nhánh tính năng lên GitHub
bằng lệnh đẩy nhánh thông thường. Bước hai, người đó mở Pull Request từ nhánh tính
năng về nhánh chính và ghi rõ mục tiêu cùng cách kiểm thử. Bước ba, ít nhất một thành
viên khác đọc thay đổi, bình luận và yêu cầu chỉnh sửa nếu cần. Bước bốn, hệ thống kiểm
tra tự động biên dịch và chạy kiểm thử để bảo đảm nhánh không làm hỏng bản chính.
Bước năm, người có quyền hợp nhất Pull Request và xóa nhánh tính năng sau khi mọi
điều kiện đều đạt.
Ví dụ sau đây minh họa toàn bộ vòng đời trên bằng dòng lệnh và công cụ dòng lệnh
của GitHub. Các chú thích trong khối lệnh được viết không dấu theo đúng quy tắc của
báo cáo. Khối lệnh giả định kho chứa đồ án đã tồn tại và máy đã đăng nhập GitHub.
1 # Clone the sample ASPX project from GitHub
2 git clone https :// github . com / lop - aspx / AspxDemo - NET481 . git
56

---

## [Page 58] (`page-58.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
3 cd AspxDemo - NET481
4
5 # Create a feature branch for login validation
6 git checkout -b feature /login - validation
7
8 # Edit Login . aspx and Login . aspx . cs in Visual Studio here ,
9 # then check status and review the diff before commit
10 git status
11 git diff -- Login . aspx Login . aspx . cs
12
13 # Commit with a Conventional Commits message
14 git add Login . aspx Login . aspx . cs
15 git commit -m " feat : validate empty username on login form "
16 git push -u origin feature /login - validation
17
18 # Open a pull request from feature branch to main
19 gh pr create -- base main -- head feature /login - validation \
20 -- title " Validate login input " \
21 -- body " Check empty username and password . Close #12. "
22
23 # Show pull request status and checks from terminal
24 gh pr status
25 gh pr checks -- watch
Hình dưới đây tóm tắt luồng năm bước của Pull Request từ lúc đẩy nhánh đến lúc
hợp nhất. Nếu người đánh giá yêu cầu thay đổi, tác giả bổ sung commit mới trên cùng
nhánh và vòng đánh giá lặp lại. Nếu kiểm tra tự động báo lỗi, Pull Request bị chặn hợp
nhất cho đến khi bản sửa được đẩy lên. Nhờ vòng lặp này, nhánh chính luôn ở trạng thái
biên dịch được và chạy được.
Day nhanh Mo PR Review Chay CI Merge
Hình 8: Luong Pull Request 5 buoc tren GitHub
Luồng Fork cũng kết thúc bằng Pull Request nhưng điểm xuất phát khác với luồng
Branch. Người đóng góp sao chép kho gốc về tài khoản của mình, tạo nhánh trên bản sao
rồi mở Pull Request ngược về kho gốc. Chủ kho gốc xem xét, chạy kiểm tra tự động và
quyết định có hợp nhất hay không. Mô hình này phổ biến trong dự án mã nguồn mở và
được mô tả kỹ trong các hướng dẫn về quy trình phân nhánh [4]. Đồ án môn học ít dùng
Fork cho việc hằng ngày nhưng sinh viên vẫn cần hiểu để có thể đóng góp cho dự án mở
sau này.
57

---

## [Page 59] (`page-59.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
4.4 Đánh giá code: approve, request changes và suggest
Đánh giá code là bước mà thành viên khác đọc kỹ thay đổi trong Pull Request trước khi
cho phép hợp nhất. GitHub cung cấp ba kết quả đánh giá chính là chấp thuận, yêu cầu
thay đổi và chỉ bình luận góp ý. Chấp thuận nghĩa là người đánh giá đồng ý cho hợp nhất,
có thể kèm góp ý nhỏ không bắt buộc. Yêu cầu thay đổi nghĩa là Pull Request chưa đạt
và tác giả bắt buộc phải sửa rồi gửi đánh giá lại. Bình luận đơn thuần dùng khi người
đọc chỉ nêu câu hỏi hoặc gợi ý mà chưa kết luận cuối cùng.
Chất lượng bình luận đánh giá quyết định hiệu quả của cả quy trình cộng tác. Bình
luận tốt nêu rõ vị trí, lý do và hướng sửa thay vì chỉ ghi chung chung là code chưa ổn. Ví
dụ thay vì ghi hàm này viết chưa tốt, người đánh giá ghi nên kiểm tra chuỗi rỗng trước
khi gọi cơ sở dữ liệu để tránh ngoại lệ. Bình luận cũng nên phân biệt lỗi bắt buộc sửa
và gợi ý cải tiến để tác giả biết ưu tiên việc nào trước. Thái độ trao đổi cần xây dựng vì
mục tiêu chung là giữ nhánh chính ổn định chứ không phải chê bai cá nhân.
Tính năng gợi ý thay đổi cho phép người đánh giá viết sẵn đoạn code thay thế ngay
trong bình luận. Tác giả chỉ cần bấm chấp nhận là gợi ý được ghi thành commit mới trên
cùng nhánh. Tính năng này rất tiện cho các sửa nhỏ như đổi tên biến, thêm kiểm tra
rỗng hay sửa chính tả thông báo. Với các sửa lớn ảnh hưởng logic, người đánh giá nên mô
tả bằng lời để tác giả chủ động sửa và kiểm thử lại. Mọi trao đổi đều lưu lại trong Pull
Request nên cuối kỳ nhóm có thể trích dẫn làm minh chứng phản biện.
Ví dụ sau đây là đoạn trích trang đăng nhập trong đồ án ASPX sau khi đã áp dụng
góp ý đánh giá. Đoạn code kiểm tra tên đăng nhập và mật khẩu ngay khi người dùng
bấm nút đăng nhập. Nếu dữ liệu rỗng hoặc mật khẩu quá ngắn, trang hiển thị thông báo
và dừng lại mà không gọi cơ sở dữ liệu. Phần chú thích trong code được viết không dấu
để giữ đúng quy tắc mã nguồn ASCII của báo cáo.
1 // Login . aspx . cs - validate input before calling the database
2 protected void btnLogin_Click ( object sender , EventArgs e )
3 {
4 string username = txtUsername . Text . Trim () ;
5 string password = txtPassword . Text ;
6
7 // Reject empty input early
8 if ( string . IsNullOrEmpty ( username ) || string . IsNullOrEmpty (
password ) )
9 {
10 lblMessage . Text = " Username and password are required . " ;
11 return ;
12 }
13
14 // Enforce a minimum password length
58

---

## [Page 60] (`page-60.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
15 if ( password . Length < 6)
16 {
17 lblMessage . Text = " Password must have at least 6
characters . " ;
18 return ;
19 }
20
21 // Next step : check the account with Membership provider
22 bool ok = System . Web . Security . Membership . ValidateUser (
username , password ) ;
23 if ( ok )
24 {
25 System . Web . Security . FormsAuthentication .
RedirectFromLoginPage ( username , false ) ;
26 }
27 else
28 {
29 lblMessage . Text = " Invalid username or password . " ;
30 }
31 }
Một bình luận đánh giá tốt cho đoạn code trên có thể viết theo cấu trúc khen đúng,
nêu vấn đề và gợi ý sửa. Ví dụ người đánh giá viết rằng việc cắt khoảng trắng và kiểm
tra rỗng là đúng hướng cho trang đăng nhập. Sau đó người đó nhận xét rằng thông báo
lỗi nên phân biệt rõ tên đăng nhập sai hay mật khẩu sai trong môi trường học tập. Cuối
cùng người đó gợi ý dùng hằng số cho độ dài tối thiểu thay vì ghi trực tiếp số 6 trong
code. Tác giả trả lời từng ý, đẩy commit sửa và nhờ đánh giá lại cho đến khi Pull Request
được chấp thuận.
Nhóm ba sinh viên nên thống nhất checklist đánh giá chung cho mọi Pull Request của
đồ án ASPX. Checklist gồm các mục như code biên dịch được, không còn mật khẩu thật,
đã kiểm tra dữ liệu rỗng và đã cập nhật tài liệu. Người đánh giá tick từng mục rồi mới
bấm chấp thuận để tránh bỏ sót lỗi quen thuộc. Với file cấu hình như Web.config, người
đánh giá phải kiểm tra kỹ vì một thẻ sai có thể làm sập toàn bộ trang. Quy trình này
tuy mất thêm thời gian nhưng giúp điểm đồ án ổn định hơn nhiều so với việc hợp nhất
vội vàng.
4.5 Bảo vệ nhánh và CODEOWNERS
Bảo vệ nhánh là tập hợp quy tắc ngăn việc đẩy trực tiếp hoặc hợp nhất vội vàng vào
nhánh quan trọng. Trên GitHub, nhóm thường bật bảo vệ cho nhánh main và nhánh
develop của đồ án ASPX. Khi đã bật, mọi thay đổi đều phải đi qua Pull Request và đáp
59

---

## [Page 61] (`page-61.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
ứng đủ điều kiện mới được hợp nhất. Nhờ vậy một commit lỗi lúc nửa đêm không thể
làm hỏng bản demo trước buổi thuyết trình.
Hai quy tắc quan trọng nhất là số lượt đánh giá bắt buộc và các kiểm tra trạng thái
bắt buộc. Quy tắc đánh giá yêu cầu ít nhất một người khác chấp thuận trước khi nút hợp
nhất được mở. Nhóm có thể yêu cầu chủ sở hữu code phải đánh giá, nghĩa là đúng người
phụ trách module đó phải duyệt. Quy tắc kiểm tra trạng thái yêu cầu các công việc tự
động như biên dịch và kiểm thử đều phải báo thành công. Tài liệu GitHub Actions mô tả
cách gắn các công việc này vào Pull Request để chặn hợp nhất khi còn lỗi [5].
Ngoài hai quy tắc trên, nhóm nên bật thêm một số tùy chọn nâng cao cho nhánh
chính. Tùy chọn yêu cầu nhánh phải cập nhật mới nhất buộc tác giả phải kéo bản mới
nhất trước khi hợp nhất. Tùy chọn cấm đẩy trực tiếp ngăn cả quản trị viên vô tình đẩy
nhầm lên nhánh chính. Tùy chọn yêu cầu hội thoại phải được giải quyết bảo đảm mọi
bình luận đánh giá đều đã có trả lời. Tùy chọn hạn chế người được đẩy giúp nhánh phát
hành chỉ do một hoặc hai thành viên phụ trách.
File CODEOWNERS cho phép khai báo ai là chủ sở hữu của từng thư mục hoặc loại
file trong kho chứa. Khi Pull Request chạm vào file thuộc phạm vi nào, GitHub tự động
gán đúng chủ sở hữu đó vào danh sách người đánh giá. Ví dụ yêu cầu của nhóm là mọi
thay đổi trong thư mục quản trị đều phải do thành viên thứ hai xem xét. Khi đó nhóm
tạo file CODEOWNERS ở thư mục gốc hoặc trong thư mục .github với nội dung như
khối dưới đây. Các dòng chú thích trong file được viết không dấu để giữ đúng quy tắc
ASCII.
1 # CODEOWNERS - owners for the ASPX course project
2 # Every change in / Admin / needs a review from TV2
3 / Admin / @TV2
4
5 # ASPX pages need reviews from TV2 and TV3
6 *. aspx @TV2 @TV3
7
8 # Code behind files need a review from TV1
9 *. aspx . cs @TV1 @TV2
10
11 # Config and workflow files need two reviewers
12 / Web . config @TV1 @TV2
13 /. github / @TV2
Khi file trên có hiệu lực, một Pull Request sửa trang trong thư mục Admin sẽ tự động
yêu cầu TV2 đánh giá. Nếu TV2 chưa chấp thuận, nút hợp nhất vẫn bị chặn cho dù các
thành viên khác đã đồng ý. Cách làm này bảo đảm người hiểu rõ module quản trị luôn
được đọc qua thay đổi liên quan. Nhóm nên đặt tên tài khoản GitHub thật thay cho ký
hiệu TV2 trước khi nộp bài. Ví dụ nếu TV2 có tài khoản là nguyen-van-b thì dòng tương
60

---

## [Page 62] (`page-62.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
ứng ghi /Admin/ kèm tên tài khoản đó.
Quy trình chuẩn cho đồ án môn học có thể tóm tắt thành một câu dễ nhớ cho cả ba
thành viên. Không ai đẩy thẳng lên nhánh chính, mọi việc đều đi qua Pull Request có
đánh giá và kiểm tra tự động. Thành viên thứ nhất phụ trách hạ tầng Git và file cấu
hình, thành viên thứ hai phụ trách GitHub và luồng hợp nhất. Thành viên thứ ba phụ
trách tổng hợp báo cáo và đối chiếu với phía GitLab trong chương sau. Nhờ kỷ luật này,
lịch sử kho chứa luôn sạch, dễ truy vết và đủ minh chứng cho phần thuyết trình.
4.6 Khái niệm: workflow, job, step, runner và trigger
GitHub Actions là nền tảng tích hợp liên tục (Continuous Integration, viết tắt là CI) và
phân phối liên tục (Continuous Delivery, viết tắt là CD) được tích hợp sẵn trong GitHub.
Mỗi khi có sự kiện như đẩy code (push) hoặc mở pull request, GitHub tự động thực hiện
một chuỗi công việc kiểm tra, biên dịch và kiểm thử đã được mô tả sẵn [5].
Đơn vị cấu hình nhỏ nhất là một tệp tin YAML đặt trong thư mục .github/workflows
của repository, ví dụ ci-aspx-481.yml. Khi tệp tin này tồn tại trên nhánh mặc định, thẻ
Actions trên GitHub sẽ liệt kê lịch sử chạy, nhật ký từng bước và kết quả đạt hay không
đạt của mỗi lần chạy.
Workflow Một tiến trình tự động hoàn chỉnh, được định nghĩa bởi một tệp tin YAML.
Ví dụ: workflow CI ASPX 4.8.1 chạy mỗi khi có push hoặc pull_request. Một
repository có thể chứa nhiều workflow chạy độc lập cho các mục đích khác nhau.
Job Một công việc lớn trong workflow, gồm nhiều bước chạy nối tiếp trên cùng một máy
ảo. Các job mặc định chạy song song; dùng needs để bắt job kiểm thử đợi job biên
dịch xong. Ví dụ: job build biên dịch solution, job test chạy kiểm thử đơn vị.
Step Một bước nhỏ trong job, hoặc chạy lệnh shell qua run hoặc tái sử dụng hành động
có sẵn qua uses. Ví dụ: bước khôi phục gói chạy lệnh nuget restore, bước kiểm
thử chạy vstest.console.exe. Mỗi bước có nhật ký riêng nên khi lỗi rất dễ xác
định bước nào gây ra.
Runner Máy ảo hoặc máy thật thực thi job, do GitHub cung cấp hoặc nhóm tự quản
lý. Project ASPX 4.8.1 bắt buộc dùng runner windows-latest vì cần MSBuild và
.NET Framework. Runner Ubuntu không biên dịch được project Web Forms dùng
.NET Framework truyền thống.
Trigger Sự kiện khởi động workflow, khai báo trong khối on của tệp tin YAML. Hai
trigger phổ biến nhất là push và pull_request kèm bộ lọc nhánh. Ngoài ra còn
trigger lịch định kỳ, trigger thủ công và trigger khi phát hành phiên bản mới.
Ba trigger được dùng nhiều nhất trong đồ án môn học là:
61

---

## [Page 63] (`page-63.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
• push lên các nhánh main và develop để kiểm tra mọi commit mới.
• pull_request nhắm vào nhánh main để kiểm tra code trước khi hợp nhất.
• Kích hoạt thủ công để chạy lại pipeline khi cần kiểm tra gấp mà không đẩy commit
mới.
Hiểu rõ năm khái niệm trên giúp đọc được mọi tệp tin workflow: trigger quyết định
khi nào chạy, runner quyết định chạy ở đâu, còn job và step quyết định chạy cái gì theo
thứ tự nào. Phần tiếp theo trình bày một workflow CI hoàn chỉnh cho project ASPX 4.8.1
từ khâu lấy code, khôi phục gói NuGet, biên dịch, kiểm thử đến lưu trữ kết quả.
4.7 Workflow CI đầy đủ cho ASPX 4.8.1
4.7.1 Tệp workflow hoàn chỉnh
Tệp tin ci-aspx-481.yml dưới đây là workflow CI hoàn chỉnh cho một solution ASP.NET
Web Forms viết bằng C# với mục tiêu .NET Framework 4.8.1. Workflow chạy trên runner
windows-latest, gồm tám bước: lấy code, cài MSBuild, cài NuGet, dùng cache, khôi phục
gói, biên dịch chế độ Release, chạy kiểm thử và tải kết quả lên artifact. Mỗi bước đều có
chú thích tiếng Anh để tương thích với quy tắc chỉ dùng ký tự ASCII trong khối liệt kê
code.
1 name : CI ASPX 4.8.1
2
3 # Trigger : run on push and pull requests to main branches .
4 on :
5 push :
6 branches : [ main , develop ]
7 pull_request :
8 branches : [ main ]
9
10 # Cancel older runs of the same branch or pull request .
11 concurrency :
12 group : ci - $ {{ github . ref }}
13 cancel - in - progress : true
14
15 jobs :
16 build :
17 # .NET Framework 4.8.1 requires a Windows runner .
18 runs - on : windows - latest
19
20 steps :
62

---

## [Page 64] (`page-64.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
21 # Step 1: check out the repository source code .
22 - name : Checkout code
23 uses : actions / checkout@v4
24
25 # Step 2: install MSBuild on the runner PATH .
26 - name : Setup MSBuild
27 uses : microsoft / setup - msbuild@v2
28
29 # Step 3: install NuGet CLI on the runner PATH .
30 - name : Setup NuGet
31 uses : nuget / setup - nuget@v2
32
33 # Step 4: restore the NuGet cache to speed up restore .
34 - name : Cache NuGet packages
35 uses : actions / cache@v4
36 with :
37 path : ~/. nuget / packages
38 key : nuget - $ {{ runner . os }} - $ {{ hashFiles (’**/ packages .
lock . json ’) }}
39 restore - keys : |
40 nuget - $ {{ runner . os }} -
41
42 # Step 5: restore all NuGet packages for the solution .
43 - name : Restore NuGet packages
44 run : nuget restore AspxDemo . sln
45
46 # Step 6: build the solution in Release mode .
47 - name : Build solution
48 run : msbuild AspxDemo . sln / p : Configuration = Release / p :
Platform ="Any CPU"
49
50 # Step 7: run unit tests with VSTest .
51 - name : Run tests
52 run : vstest . console . exe Tests \ bin \ Release \ AspxDemo . Tests .
dll / Logger : trx
53
54 # Step 8: upload the published site as an artifact .
55 - name : Upload artifact
56 uses : actions / upload - artifact@v4
57 with :
58 name : aspx - site
63

---

## [Page 65] (`page-65.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
59 path : WebApp \ obj \ Release \ Package
60 retention - days : 7
Listing 24: Workflow CI đầy đủ cho project ASPX 4.8.1
Workflow trên có thể sao chép vào thư mục .github/workflows của repository demo
và chạy ngay sau khi đẩy lên GitHub, với điều kiện solution có tên AspxDemo.sln và
project kiểm thử đã được biên dịch ra AspxDemo.Tests.dll.
4.7.2 Giải thích từng bước
1. Lấy code: hành động actions/checkout@v4 tải mã nguồn tại đúng commit kích
hoạt. Không có bước này, các bước sau không có code để biên dịch và kiểm thử.
2. Cài MSBuild: hành động microsoft/setup-msbuild@v2 đưa MSBuild.exe vào
biến PATH. MSBuild là công cụ duy nhất biên dịch đầy đủ project Web Forms mục
tiêu .NET Framework 4.8.1.
3. Cài NuGet: hành động nuget/setup-nuget@v2 đưa nuget.exe vào biến PATH.
Lệnh nuget restore sau đó đọc packages.config và tải các gói còn thiếu về máy
chạy.
4. Dùng cache: hành động actions/cache@v4 lưu thư mục ~/.nuget/packages giữa
các lần chạy. Khóa cache gồm hệ điều hành và giá trị băm của tệp khóa gói nên khi
không đổi thư viện thì bỏ qua tải lại.
5. Khôi phục gói: lệnh nuget restore AspxDemo.sln tải phần gói còn thiếu sau khi
đã dùng cache. Bước này bắt buộc đứng trước biên dịch, nếu thiếu gói thì MSBuild
sẽ báo lỗi ngay.
6. Biên dịch: lệnh msbuild AspxDemo.sln /p:Configuration=Release biên dịch
toàn bộ solution. Mọi lỗi biên dịch làm workflow báo đỏ và chặn pull request cho
đến khi được sửa.
7. Kiểm thử: lệnh vstest.console.exe chạy các DLL kiểm thử và xuất nhật ký
định dạng .trx. Chỉ cần một test không đạt, toàn bộ workflow được đánh dấu thất
bại.
8. Lưu artifact: hành động actions/upload-artifact@v4 lưu gói triển khai trong
7 ngày. Dùng tham số retention-days để kiểm soát dung lượng lưu trữ của repos￾itory.
Với tám bước trên, mọi pull request đều được biên dịch và kiểm thử tự động trước khi
review. Nhóm nên bật quy tắc yêu cầu workflow đạt mới được hợp nhất để nhánh chính
luôn biên dịch được. Phần tiếp theo trình bày cách quản lý secret và môi trường triển
khai an toàn.
64

---

## [Page 66] (`page-66.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
4.8 Secrets và Environments
Secret là biến môi trường được mã hóa, dùng để lưu thông tin nhạy cảm như chuỗi kết
nối cơ sở dữ liệu, mật khẩu tài khoản triển khai hoặc khóa ký gói. Giá trị secret không
bao giờ hiển thị trong nhật ký: GitHub tự động che thành *** khi secret vô tình được in
ra. Khai báo secret tại thẻ Settings, mục Secrets and variables, nút New repository secret;
secret cấp môi trường thì khai báo trong từng environment.
• Secret cấp repository: mọi workflow trong repository đều đọc được. Dùng cho khóa
dùng chung như token đọc gói nội bộ của nhóm.
• Secret cấp môi trường: chỉ workflow gắn đúng environment mới đọc được. Dùng cho
chuỗi kết nối, vì staging và production dùng cơ sở dữ liệu khác nhau.
• Biến môi trường thường: giá trị hiển thị công khai trong nhật ký. Chỉ dùng cho dữ
liệu không nhạy cảm như tên thư mục đầu ra hoặc cờ bật chi tiết nhật ký.
Trong tệp tin YAML, đọc secret bằng cú pháp ${{ secrets.TEN_SECRET }}, ví dụ
${{ secrets.STAGING_CONN_STRING }}. Cú pháp này do GitHub thay thế lúc chạy, nên
tuyệt đối không ghi giá trị thật vào code mà chỉ ghi tên secret. Tài liệu chính thức tại
https://docs.github.com/actions mô tả đầy đủ cú pháp và phạm vi áp dụng.
1 jobs :
2 deploy - staging :
3 # Deploy job bound to the staging environment .
4 runs - on : windows - latest
5 environment : staging
6 steps :
7 # Read the staging connection string from secrets .
8 - name : Deploy to staging
9 run : deploy . cmd $ {{ secrets . STAGING_CONN_STRING }}
10 deploy - production :
11 # Production requires manual approval in settings .
12 runs - on : windows - latest
13 environment : production
14 steps :
15 # Read the production connection string from secrets .
16 - name : Deploy to production
17 run : deploy . cmd $ {{ secrets . PROD_CONN_STRING }}
Listing 25: Đọc secret theo môi trường staging và production
Environment gom secret, quy tắc bảo vệ và lịch sử triển khai của một môi trường. Môi
trường staging cho phép triển khai tự động mỗi khi hợp nhất vào nhánh develop để kiểm
65

---

## [Page 67] (`page-67.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
thử sớm. Môi trường production yêu cầu ít nhất một người review phê duyệt trước khi
triển khai, đồng thời giới hạn chỉ nhánh chính mới được triển khai để tránh phát hành
nhầm code thử nghiệm.
• Không bao giờ đẩy tệp tin chứa secret thật như bản Web.config trên máy cá nhân
lên repository.
• Xoay vòng secret ngay khi thành viên rời nhóm hoặc nghi ngờ lộ, rồi cập nhật lại
trên GitHub.
• Dùng secret khác nhau cho staging và production để lộ môi trường thử nghiệm
không ảnh hưởng hệ thống thật.
4.9 Cache NuGet và artifacts
Mỗi lần pipeline chạy, lệnh khôi phục gói phải tải hàng trăm MB thư viện từ Internet,
chiếm phần lớn thời gian và dễ thất bại khi mạng chậm. Cache lưu thư mục gói toàn cục
~/.nuget/packages sau lần chạy đầu, các lần sau chỉ tải phần thay đổi nên thường rút
ngắn bước khôi phục từ vài phút xuống còn vài chục giây [6].
Khóa cache gồm tên hệ điều hành và giá trị băm của các tệp tin khóa gói như
packages.lock.json hoặc packages.config. Khi không đổi thư viện, khóa trùng khớp
và cache được dùng lại; khi thêm hoặc nâng cấp gói, khóa thay đổi nên cache cũ bị bỏ,
đồng thời khóa dự phòng bảo đảm vẫn tái sử dụng được phần lớn gói đã lưu.
1 steps :
2 # Cache the global NuGet folder between runs .
3 - name : Cache NuGet packages
4 uses : actions / cache@v4
5 with :
6 path : ~/. nuget / packages
7 key : nuget - $ {{ runner . os }} - $ {{ hashFiles (’**/*. csproj ’, ’
**/ packages . config ’) }}
8 restore - keys : |
9 nuget - $ {{ runner . os }} -
10
11 # Packages missing from cache are downloaded by restore .
12 - name : Restore packages
13 run : nuget restore AspxDemo . sln
14
15 # Keep the build output for download and deploy jobs .
16 - name : Upload test results
17 uses : actions / upload - artifact@v4
18 with :
66

---

## [Page 68] (`page-68.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
19 name : test - results
20 path : TestResults /*. trx
Listing 26: Cache NuGet và tải kết quả kiểm thử lên artifact
Artifact là nơi lưu kết quả đầu ra của pipeline: gói triển khai website, tệp tin nhật
ký kiểm thử định dạng .trx hoặc bản dựng để job triển khai tải về dùng tiếp. Khác với
cache vốn có thể bị xóa bất cứ lúc nào, artifact được đảm bảo tồn tại đúng số ngày đã
cấu hình qua retention-days. Nhờ artifact, thành viên review có thể tải đúng bản đã
kiểm thử về chạy thử mà không cần biên dịch lại.
• Luôn đặt cache ngay trước bước khôi phục gói để bước này hưởng lợi trực tiếp.
• Đưa tệp tin khóa gói vào repository để khóa cache ổn định giữa các lần chạy.
• Chỉ tải artifact thật sự cần thiết và đặt thời gian lưu ngắn để tiết kiệm dung lượng.
4.10 Runner Windows và Ubuntu cho .NET Framework 4.8.1
Project ASP.NET Web Forms mục tiêu .NET Framework 4.8.1 chỉ biên dịch đầy đủ trên
Windows, vì bộ công cụ gồm MSBuild, trình biên dịch trang ASPX và thư viện tham
chiếu .NET Framework đều là thành phần gắn chặt với hệ điều hành Windows [9]. Nền
tảng .NET Framework khác với .NET hiện đại đa nền tảng: thư viện và công cụ của nó
không có bản Linux [10].
Runner ubuntu-latest khởi động nhanh và miễn phí nhiều phút hơn, nhưng không có
MSBuild đầy đủ, không có .NET Framework 4.8.1 và không chạy được vstest.console.exe.
Lệnh dotnet build trên Ubuntu chỉ biên dịch project SDK-style dùng .NET hiện đại,
không hiểu project Web Forms kiểu cũ với tệp tin packages.config và quy trình biên
dịch trang ASPX.
67

---

## [Page 69] (`page-69.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Bảng 12: So sánh runner cho project ASPX 4.8.1
Tiêu chí Runner Windows Runner Ubuntu
Hệ điều hành Windows Server 2022 Ubuntu 22.04
MSBuild đầy đủ Có sẵn qua
setup-msbuild
Không có
Biên dịch .NET
Framework 4.8.1
Hỗ trợ đầy đủ Không hỗ trợ
Trang ASPX Web
Forms
Biên dịch được Không biên dịch được
Kiểm thử VSTest Chạy được Không chạy được
Tốc độ và chi phí Khởi động chậm hơn Nhanh và rẻ hơn
Khuyến nghị Bắt buộc cho ASPX
4.8.1
Chỉ dùng cho .NET
hiện đại
Bảng 12 tóm tắt sự khác biệt: với project ASPX 4.8.1, runner Windows là lựa chọn
bắt buộc, dù tốn thời gian khởi động hơn. Hình 9 minh họa chuỗi công việc CI chạy trên
runner này từ lúc lấy code đến khi có artifact.
Checkout Restore Build Test
push cache pass
Hình 9: Chuỗi công việc CI cho project ASPX trên runner Windows
Tóm lại, GitHub Actions giúp nhóm ASPX tự động hóa toàn bộ vòng kiểm tra mỗi
khi đẩy code, với điều kiện chọn đúng runner Windows cho .NET Framework 4.8.1. Kết
hợp workflow CI đạt, secret quản lý tập trung và cache hợp lý, nhóm có thể hợp nhất pull
request nhanh mà vẫn an toàn.
4.11 Packages và Pages: gói NuGet nội bộ và trang tài liệu
GitHub không chỉ lưu mã nguồn mà còn cung cấp kho gói tích hợp mang tên GitHub
Packages, cho phép nhóm đồ án publish các thư viện dùng chung ở dạng gói *.nupkg thay
vì chép file .dll thủ công qua USB hay email. Mỗi gói gắn với một repository, kế thừa
quyền truy cập của repository đó, nên thành viên nào đọc được code thì mới tải được gói
nội bộ [6].
Quy trình publish gói cho project ASP.NET Web Forms gồm ba bước chính: đóng gói
project thư viện bằng dotnet pack hoặc nuget pack, thêm nguồn gói trỏ về nuget.pkg.github.com,
rồi đẩy gói lên bằng dotnet nuget push với token xác thực GITHUB_TOKEN. Token này
cần quyền write:packages, còn khi cài gói chỉ cần quyền read:packages nên rất phù
hợp để cấp cho máy cá nhân của từng thành viên mà không lo lộ quyền ghi [6].
68

---

## [Page 70] (`page-70.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
1 # Buoc 1: dong goi thu vien dung chung ( ASCII only comments )
2 dotnet pack MyLib / MyLib . csproj -c Release -o ./ nupkg
3 # Buoc 2: them nguon GitHub Packages ( OWNER = ten user hoac org )
4 dotnet nuget add source https :// nuget . pkg . github . com / OWNER / index .
json \
5 -- name github -- username OWNER -- password $GITHUB_TOKEN -- store
- password -in - clear - text
6 # Buoc 3: day goi len GitHub Packages
7 dotnet nuget push ./ nupkg / MyLib .1.0.0. nupkg -- source github
8 # Cai goi tu may thanh vien khac trong nhom
9 dotnet add package MyLib -- version 1.0.0 -- source https :// nuget .
pkg . github . com / OWNER / index . json
Với project Web Forms trên .NET Framework 4.8.1, lệnh dotnet pack không dùng
trực tiếp cho project .aspx mà dùng cho project thư viện Class Library đi kèm, ví dụ
project chứa lớp tiện ích mã hóa mật khẩu hay lớp phân trang dùng chung cho ba thành
viên [10]. Phiên bản gói nên đặt theo quy tắc Semantic Versioning, ví dụ 1.2.0, kết hợp
Conventional Commits để sinh changelog tự động [3].
GitHub Pages là dịch vụ host trang web tĩnh miễn phí ngay từ repository, rất phù
hợp để công bố tài liệu đồ án: đặc tả yêu cầu, sơ đồ cơ sở dữ liệu, hướng dẫn cài
đặt và nhật ký demo từng tuần. Nhóm chỉ cần đưa file HTML tĩnh hoặc source Jekyll
vào nhánh main hoặc thư mục docs, bật Pages trong phần Settings là có ngay địa chỉ
https://nhom3tuhoc.github.io/AspxDemo-NET481/ để nộp kèm báo cáo.
Cách hiện đại nhất là deploy Pages bằng GitHub Actions: mỗi lần merge vào nhánh
main, workflow tự động build tài liệu và publish, khỏi cần giữ nhánh gh-pages thủ công
như trước đây [5]. Ví dụ tối thiểu dưới đây build thư mục docs và đẩy lên Pages:
1 # Workflow deploy tai lieu do an len GitHub Pages
2 name : docs - to - pages
3 on :
4 push :
5 branches : [ main ]
6 paths : [’docs /** ’]
7 permissions :
8 contents : read
9 pages : write
10 id - token : write
11 jobs :
12 deploy :
13 runs - on : ubuntu - latest
14 environment :
69

---

## [Page 71] (`page-71.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
15 name : github - pages
16 steps :
17 - uses : actions / checkout@v4
18 - uses : actions / configure - pages@v5
19 - uses : actions / upload - pages - artifact@v3
20 with :
21 path : docs
22 - uses : actions / deploy - pages@v4
Tóm lại, Packages giải quyết bài toán chia sẻ thư viện nội bộ có phiên bản, còn Pages
giải quyết bài toán công bố tài liệu công khai với chi phí bằng không. Cả hai đều tận
dụng sẵn quyền truy cập của repository nên nhóm không cần dựng thêm server riêng
trong phạm vi đồ án môn học.
4.12 Codespaces: môi trường phát triển trên mây
GitHub Codespaces là môi trường phát triển đầy đủ chạy trên mây, mở trực tiếp từ
repository bằng trình duyệt hoặc Visual Studio Code [6]. Mỗi codespace là một container
có sẵn Git, .NET SDK, Node và các extension, được mô tả bằng file devcontainer.json
nên mọi thành viên mở lên đều có môi trường giống hệt nhau, chấm dứt cảnh máy chạy
được máy thì không.
Với đồ án ASP.NET Web Forms 4.8.1, cần lưu ý Codespaces chạy trên Linux nên
không build trực tiếp project Web Forms vốn cần MSBuild trên Windows. Nhóm vẫn
dùng Codespaces hiệu quả cho các việc không cần build Windows: viết báo cáo LaTeX,
soạn tài liệu, review pull request, viết YAML cho Actions và chạy các script kiểm tra
chính tả hay kiểm tra link hỏng [9]. Việc build thật project .aspx vẫn giao cho GitHub
Actions với runner windows-latest, như vậy mỗi người đóng góp đúng thế mạnh của
từng nền tảng.
Ba thao tác Codespaces dùng nhiều nhất trong đồ án:
• Tạo codespace mới từ nhánh main hoặc từ một pull request để review code.
• Mở terminal trong codespace, chạy git status và git log như máy local.
• Commit và push về repository, pipeline Actions tự động chạy kiểm tra.
1 # Cai dat CLI de dieu khien Codespaces tu terminal
2 gh extension install github / gh - codespace
3 # Liet ke cac codespace hien co
4 gh codespace list
5 # Tao codespace moi tu repo do an ( nhanh main )
6 gh codespace create -- repo OWNER / AspxDemo_NET481 -- branch main
70

---

## [Page 72] (`page-72.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
7 # Mo SSH vao codespace de lam viec
8 gh codespace ssh -- codespace my - codespace - name
9 # Xoa codespace khi xong viec de tiet kiem quota
10 gh codespace delete -- codespace my - codespace - name
Codespaces git push Actions
commit build
Hình 10: Luong lam viec tu Codespaces den Actions
Hình trên tóm tắt luồng làm việc: soạn thảo trên Codespaces, đẩy code về repository,
Actions trên runner Windows build project ASPX 4.8.1 và báo kết quả. Sinh viên dùng
gói GitHub Education được cấp quota Codespaces miễn phí mỗi tháng, đủ cho nhu cầu
viết tài liệu và review code của đồ án (xem mục Giáo dục ở cuối).
4.13 Copilot: trợ lý gợi ý code bằng AI
Muse là trợ lý lập trình dùng mô hình ngôn ngữ lớn, gợi ý ngay trong editor khi sinh
viên gõ comment hoặc tên hàm [6]. Với đồ án Web Forms, Copilot giúp sinh code lặp lại
nhanh hơn khoảng 30%, ví dụ tạo validator, sinh truy vấn, viết unit test cho lớp tiện ích.
Tuy nhiên Copilot chỉ gợi ý chứ không hiểu nghiệp vụ, nên mọi đoạn code sinh ra đều
phải đọc lại, chạy thử và review như code của người viết.
Ví dụ: sinh viên gõ comment mô tả hàm kiểm tra đăng nhập, Copilot gợi ý khung
hàm C# kiểm tra tên đăng nhập và mật khẩu cho trang Login.aspx. Đoạn code dưới
đây mô phỏng kết quả gợi ý sau khi đã chỉnh sửa để an toàn hơn:
1 // Check login for page Login . aspx ( demo only )
2 public bool KiemTraDangNhap ( string tenDangNhap , string matKhau )
3 {
4 if ( string . IsNullOrWhiteSpace ( tenDangNhap ) ) return false ;
5 if ( string . IsNullOrEmpty ( matKhau ) ) return false ;
6 string sql = " SELECT MatKhauHash , Muoi FROM NguoiDung WHERE
TenDangNhap = @u " ;
7 using ( var conn = new SqlConnection ( _chuoiKetNoi ) )
8 using ( var cmd = new SqlCommand ( sql , conn ) )
9 {
10 cmd . Parameters . AddWithValue ( " @u " , tenDangNhap ) ;
11 conn . Open () ;
12 using ( var rd = cmd . ExecuteReader () )
13 {
14 if (! rd . Read () ) return false ;
15 string hashLuu = rd . GetString (0) ;
71

---

## [Page 73] (`page-73.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
16 string muoi = rd . GetString (1) ;
17 string hashNhap = HamBamMatKhau ( matKhau , muoi ) ;
18 return hashLuu == hashNhap ;
19 }
20 }
21 }
Ba điểm cần tự kiểm tra sau khi nhận gợi ý từ Copilot:
1. Truy vấn phải tham số hóa bằng @u như trên, tuyệt đối không nối chuỗi tên đăng
nhập vào câu lệnh SQL vì sẽ dính lỗi SQL injection.
2. Mật khẩu phải băm kèm muối bằng thuật toán mạnh, không lưu hay so sánh mật
khẩu gốc, không gắn cứng mật khẩu mẫu trong code.
3. Chuỗi kết nối lấy từ file cấu hình hoặc Secret, không dán trực tiếp vào code hay vào
prompt chat với Copilot.
Về bản quyền và bảo mật, nhóm cần nhớ ba nguyên tắc [6]:
• Không dán mã nguồn độc quyền, đề thi hay dữ liệu cá nhân vào prompt, vì nội
dung prompt có thể được dùng theo chính sách của nhà cung cấp.
• Đoạn gợi ý dài giống hệt code nổi tiếng cần kiểm tra giấy phép trước khi dùng,
tránh vi phạm bản quyền của project nguồn mở.
• Secret như token, connection string, khóa API không bao giờ xuất hiện trong
prompt, trong code mẫu hay trong lịch sử commit.
Khi dùng đúng cách, Copilot là gia sư kiên nhẫn: giải thích code khó, gợi ý test case,
đề xuất refactor tên biến rõ nghĩa hơn cho sinh viên năm nhất.
4.14 Bảo mật nâng cao: quét secret, Dependabot và CodeQL
Repository đồ án thường chứa file Web.config với chuỗi kết nối cơ sở dữ liệu, nên tính
năng bảo mật của GitHub có giá trị thực tế ngay từ buổi đầu [6]. Secret scanning tự động
quét lịch sử commit để tìm token, khóa API hay mật khẩu bị vô tình đẩy lên, rồi gửi cảnh
báo cho người maintain repository.
Mạnh hơn một bước, push protection chặn ngay tại thời điểm push: nếu commit chứa
ví dụ một connection string của SQL Server, lệnh push bị từ chối kèm hướng dẫn xóa
secret khỏi commit, thay vì để lọt lên server rồi mới cảnh báo sau. Ví dụ dưới đây mô
phỏng lần push bị chặn và cách khắc phục:
72

---

## [Page 74] (`page-74.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
1 # Vo tinh commit file cau hinh chua secret that
2 git add Web . config
3 git commit -m " Update connection string "
4 git push origin feature / login
5 # Ket qua : remote tu choi vi phat hien secret ( push protection )
6 # remote : error : GH013 : Repository rule violations found for refs
/ heads / feature / login
7 # Giai phap : dua secret ra khoi code , doc tu bien moi truong
8 # 1) Xoa commit chua secret ( nhanh ca nhan , chua merge )
9 git reset -- soft HEAD ~1
10 # 2) Thay connection string that bang gia tri gia an toan
11 # 3) Commit lai va push , sau do xoay ( rotate ) secret bi lo
12 git commit -m " fix : move connection string to environment
variable "
13 git push origin feature / login
Dependabot tự động mở pull request nâng cấp các gói phụ thuộc có lỗ hổng, ví dụ
nâng cấp thư viện JavaScript trong thư mục Scripts hay gói NuGet cũ trong project
packages.config [6]. Nhóm chỉ cần review và merge pull request của Dependabot như
pull request thường, pipeline Actions sẽ build lại để xác nhận bản nâng cấp không phá
vỡ đồ án.
CodeQL là công cụ phân tích tĩnh: nó dựng cơ sở dữ liệu ngữ nghĩa của mã nguồn rồi
chạy các truy vấn tìm mẫu lỗ hổng như SQL injection hay cross-site scripting. CodeQL
chạy như một workflow Actions, báo kết quả ngay trong thẻ Security của repository, rất
phù hợp để rà soát trang đăng nhập trước buổi demo [5].
Bảng 13: Bon tinh nang bao mat nang cao cua GitHub
Tính năng Phát hiện gì Chặn ở đâu Ai xử lý
Secret scanning Token và khóa API bị lộ Sau khi push Người maintain
Push protection Secret trong commit mới Trước khi push Người push
Dependabot Gói phụ thuộc có lỗ hổng Pull request mới Người review
CodeQL Mẫu code dễ bị tấn công Workflow Actions Cả nhóm
Bảng trên giúp nhóm phân công rõ ràng: người push chịu trách nhiệm gỡ secret, người
review chịu trách nhiệm merge bản vá Dependabot, cả nhóm cùng đọc báo cáo CodeQL
trước mỗi mốc nộp bài.
73

---

## [Page 75] (`page-75.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
4.15 Gói GitHub Education cho sinh viên
GitHub Education là gói ưu đãi miễn phí dành cho sinh viên, giảng viên và nhà trường,
gom nhiều công cụ trả phí thành một gói duy nhất [6]. Với sinh viên, ba lợi ích thiết thực
nhất cho đồ án ASPX là: Copilot miễn phí trong thời gian học, quota Codespaces miễn
phí mỗi tháng và không giới hạn repository private cùng cộng tác viên cho nhóm đồ án.
Ngoài ra gói còn kèm nhiều ưu đãi từ đối tác như tên miền miễn phí, credit cloud để
demo và khóa học bổ trợ, giúp nhóm công bố sản phẩm môn học nghiêm túc mà không
tốn chi phí hạ tầng.
Các bước đăng ký gói sinh viên:
1. Chuẩn bị email do trường cấp, ví dụ email có đuôi @edu.vn hoặc @st.university.edu.vn,
kèm thẻ sinh viên hoặc giấy xác nhận đang học.
2. Truy cập trang https://education.github.com/ và chọn mục đăng ký gói Student
Developer Pack.
3. Điền thông tin trường, tải minh chứng sinh viên và chờ GitHub xét duyệt, thường
từ vài giờ đến vài ngày.
4. Sau khi được duyệt, bật Copilot và kiểm tra quota Codespaces trong phần cài đặt
tài khoản, rồi mời hai thành viên còn lại cộng tác repository đồ án.
Lưu ý: ưu đãi gắn với trạng thái sinh viên nên cần gia hạn sau mỗi chu kỳ học, khi
tốt nghiệp một số tính năng sẽ chuyển về gói miễn phí thông thường. Nhóm nên đăng ký
sớm từ đầu học kỳ để tận dụng Copilot và Codespaces cho toàn bộ quá trình làm đồ án
thay vì chờ đến tuần nộp bài mới đăng ký [6].
Như vậy, từ Packages, Pages, Codespaces, Copilot đến bộ công cụ bảo mật và gói
Education, GitHub cung cấp một hệ sinh thái khép kín cho nhóm sinh viên: viết code,
chia sẻ thư viện, công bố tài liệu, rà soát bảo mật và demo sản phẩm trên một nền tảng
duy nhất, sẵn sàng liên thông sang GitLab ở chương tiếp theo.
5 GitLab
GitLab là nền tảng DevOps tích hợp toàn diện, kết hợp quản lý mã nguồn Git, theo
dõi công việc, review code, kiểm thử và triển khai trong một ứng dụng duy nhất. Với
đồ án ASPX trên .NET Framework 4.8.1, GitLab giúp nhóm ba sinh viên làm việc trên
cùng một kho mã mà vẫn kiểm soát được chất lượng qua Merge Request, Approval rules,
protected branch và pipeline tự động. Chương này trình bày các khái niệm GitLab cơ
bản nhất mà nhóm đã dùng thật cho đồ án: Groups, Projects, Issues, Boards, Milestones,
Wiki, Snippets, Merge Request và bảo vệ nhánh. Nội dung phần CI/CD nâng cao với
74

---

## [Page 76] (`page-76.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Windows runner và msbuild được trình bày ở chương tiếp theo, để chương này tập trung
vào quy trình cộng tác hằng ngày [8].
5.1 Tổng quan GitLab: nền tảng DevOps tích hợp
GitLab đi theo triết lý DevOps Platform: một vòng đời khép kín từ ý tưởng tới vận hành.
Thay vì ghép nhiều công cụ rời rạc, nhóm chỉ cần một nơi duy nhất để lập kế hoạch, viết
code, review, kiểm thử, phát hành và giám sát. Cách tiếp cận này đặc biệt phù hợp với
đồ án môn học, vì nhóm nhỏ, thời gian ngắn, nhưng vẫn phải thể hiện được quy trình
chuyên nghiệp giống doanh nghiệp [8].
Ba trụ cột mà nhóm khai thác nhiều nhất gồm quản lý mã nguồn Git, cộng tác qua
Merge Request, và quản trị công việc qua Issues cùng Boards. Mọi thay đổi trên form
Default.aspx, code-behind Default.aspx.cs hay Web.config đều đi qua một Merge
Request có người review, thay vì đẩy thẳng lên nhánh chính. Nhờ vậy, lịch sử commit
sạch, dễ truy vết ai sửa gì, vì sao sửa, và có thể hoàn tác an toàn.
GitLab được cung cấp theo hai mô hình triển khai chính. Mô hình SaaS tại https:
//gitlab.com do GitLab vận hành sẵn, nhóm chỉ cần đăng ký tài khoản là dùng ngay.
Mô hình self-hosted cho phép khoa hoặc doanh nghiệp tự cài đặt GitLab lên máy chủ
riêng để toàn quyền kiểm soát. Bảng 14 so sánh hai mô hình theo năm tiêu chí quan trọng
với đồ án môn học [8].
Bảng 14: So sánh GitLab SaaS và GitLab self-hosted
Tiêu chí SaaS gitlab.com Self-hosted
Cài đặt và vận hành Đăng ký là dùng ngay Tự cài đặt và bảo trì máy chủ
Chi phí Miễn phí cho nhóm nhỏ Tốn máy chủ và công quản trị
Kiểm soát dữ liệu Dữ liệu đặt trên cloud Dữ liệu nằm hoàn toàn nội bộ
Runner cho ASPX 4.8.1 Dùng runner cloud có sẵn Tự gắn Windows runner riêng
Nâng cấp và tùy biến Tự động nâng cấp Chủ động chọn phiên bản
Với đồ án ASPX của nhóm, mô hình SaaS là lựa chọn hợp lý vì không tốn máy chủ,
vẫn đủ tính năng cho ba thành viên, và dễ chia sẻ link công khai cho giảng viên chấm
bài. Nhóm tạo một Group chung, bên trong là Project chứa toàn bộ source Web Forms,
bật Issues và Merge Request ngay từ đầu để mọi trao đổi đều lưu lại trên GitLab. Lệnh
dưới đây cho thấy thao tác đầu tiên của thành viên mới: clone kho về máy, tạo nhánh
tính năng và đẩy lên GitLab để chuẩn bị mở Merge Request.
1 # Clone the ASPX demo project from GitLab
2 git clone https :// gitlab . com / nhom3 / aspxdemo - net481 . git
3 cd aspxdemo - net481
4 git config user . name " Sinh Vien 3 "
75

---

## [Page 77] (`page-77.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
5 git config user . email " sv3@example . com "
6 git checkout -b feature /login - aspx
7 # Edit Default . aspx and Default . aspx . cs , then commit
8 git add Default . aspx Default . aspx . cs Web . config
9 git commit -m " feat : them form dang nhap ASPX "
10 git push -u origin feature /login - aspx
Listing 27: Clone kho ASPX và đẩy nhánh tính năng lên GitLab
Sau khi đẩy nhánh, GitLab hiển thị nút tạo Merge Request ngay trên trang Project.
Thành viên chỉ cần bấm nút, ghi mô tả thay đổi, gán reviewer là một bạn khác trong
nhóm, rồi chờ pipeline chạy và chờ approve trước khi merge. Quy trình này tuy thêm một
bước so với đẩy thẳng, nhưng loại bỏ phần lớn lỗi do sửa nhầm file dùng chung.
5.2 Groups, Projects, Issues, Boards, Milestones, Wiki, Snip￾pets
Bảy khái niệm dưới đây tạo thành bộ khung cộng tác hằng ngày của nhóm trên GitLab.
Mỗi khái niệm được giải thích gắn trực tiếp với đồ án ASPX, để người đọc hình dung
ngay cách dùng.
Groups Group là đơn vị tổ chức cao nhất mà nhóm dùng, đại diện cho cả nhóm ba
sinh viên. Nhóm đặt tên Group theo tên đề tài, thêm cả ba thành viên với vai trò
Developer, còn giảng viên được thêm với vai trò Reporter để xem code và pipeline
mà không sửa được. Mọi Project con trong Group đều kế thừa thành viên, giúp
phân quyền một lần cho tất cả kho.
Projects Project là một kho Git kèm đầy đủ Issues, Merge Request, Wiki và pipeline.
Đồ án ASPX chỉ cần một Project duy nhất chứa toàn bộ solution .NET Framework
4.8.1, gồm thư mục web, file Web.config, file solution và thư mục tài liệu. Nhóm
bật tính năng Issues, Wiki và Container Registry ngay khi tạo Project, để không
phải cấu hình rời rạc về sau.
Issues Issue là đơn vị công việc nhỏ nhất, dùng để ghi nhận việc cần làm hoặc lỗi cần
sửa. Ví dụ, khi form đăng nhập báo lỗi sai chuỗi kết nối, nhóm tạo Issue với tiêu đề
mô tả lỗi, gán nhãn bug và priority-high, rồi gán cho thành viên phụ trách xử
lý. Mỗi Issue đều có số thứ tự, người được gán, nhãn, hạn chót và luồng thảo luận
riêng. Nhờ vậy, không còn tình trạng giao việc bằng tin nhắn rồi quên mất ai làm
gì.
Boards Board là bảng Kanban trực quan, kéo thả các Issue qua các cột như To do,
Doing và Done. Nhóm họp nhanh mỗi tối, mở Board ra là thấy ngay ai đang làm
76

---

## [Page 78] (`page-78.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
dở việc gì, việc nào tắc. Khi bắt đầu sửa form đăng nhập, thành viên kéo Issue sang
cột Doing và tự gán cho mình. Khi Merge Request tương ứng được merge, Issue tự
đóng và thẻ biến mất khỏi Board. Cách làm này giúp tiến độ đồ án luôn hiển thị
công khai, không cần báo cáo thủ công.
Milestones Milestone là mốc thời gian gom nhiều Issue lại, tương ứng với một đợt nộp
bài. Nhóm đặt ba mốc: bản nháp giao diện, bản tích hợp đầy đủ chức năng, và bản
nộp cuối cùng. Mỗi Issue khi tạo đều được gắn vào một mốc, nên trang Milestone
luôn cho biết còn bao nhiêu việc chưa xong. Giảng viên chỉ cần mở trang Milestone
là đánh giá được tiến độ, thay vì phải hỏi từng thành viên.
Wiki Wiki là nơi viết tài liệu nội bộ: hướng dẫn cài môi trường, cách cấu hình IIS, cách
khôi phục cơ sở dữ liệu mẫu và danh sách tài khoản thử nghiệm. Khác với file văn
bản trong kho code, Wiki có lịch sử sửa đổi riêng và sửa trực tiếp trên trình duyệt.
Nhóm ghi vào Wiki các bước build bằng msbuild cho .NET Framework 4.8.1, để
thành viên mới chỉ cần đọc Wiki là dựng được môi trường trong một buổi.
Snippets Snippet là đoạn code hoặc cấu hình ngắn được chia sẻ nhanh trong nhóm. Ví
dụ, đoạn chuỗi kết nối mẫu, đoạn cấu hình lại Web.config hay hàm kiểm tra đăng
nhập viết bằng C#, đều được lưu thành Snippet thay vì gửi qua tin nhắn dễ thất
lạc. Mỗi Snippet có tiêu đề, định dạng ngôn ngữ và lịch sử phiên bản, dùng lại được
nhiều lần.
Khi đã quen, nhóm tạo Issue trực tiếp bằng GitLab API trong các script tự động. Ví
dụ dưới đây tạo một Issue báo lỗi xung đột Web.config bằng lệnh curl, rất hữu ích khi
pipeline phát hiện lỗi và muốn ghi nhận tự động.
1 # Create an issue via GitLab API ( needs a personal token )
2 export GITLAB_TOKEN = " glpat - xxxxxxxx "
3 export PROJECT_ID = " 12345678 "
4 curl -- request POST \
5 -- header " PRIVATE - TOKEN : $GITLAB_TOKEN " \
6 -- data " title = Fix Web . config conflict on develop " \
7 -- data " description = Merge develop gay xung dot muc
connectionStrings " \
8 -- data " labels = bug , ASPX , priority - high " \
9 " https :// gitlab . com / api / v4 / projects / $PROJECT_ID / issues "
Listing 28: Tạo Issue tự động bằng GitLab API
77

---

## [Page 79] (`page-79.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
5.3 Merge Request và Approval rules
Merge Request, viết tắt là MR, là cơ chế review code trung tâm của GitLab, tương đương
với Pull Request trên GitHub nhưng gắn chặt hơn với pipeline và Approval rules. Mọi
thay đổi cho đồ án ASPX, từ sửa giao diện tới đổi chuỗi kết nối, đều phải đi qua MR.
Quy định này giúp nhóm ba người không bao giờ ghi đè lẫn nhau trên nhánh chính.
Vòng đời điển hình của một MR trong đồ án gồm sáu bước.
1. Tạo nhánh tính năng từ develop, đặt tên rõ ràng như feature-login.
2. Viết code, commit theo Conventional Commits rồi đẩy nhánh lên GitLab.
3. Mở MR từ nhánh tính năng về develop hoặc main, ghi mô tả và ảnh chụp màn
hình.
4. Pipeline tự động chạy build và kiểm tra cơ bản trên chính MR đó.
5. Một hoặc hai thành viên khác review code, bình luận và approve.
6. Merge MR khi đủ approve và pipeline báo thành công, sau đó xóa nhánh tính năng.
Approval rules là quy tắc bắt buộc về số người phê duyệt trước khi được merge. Với
đồ án môn học, nhóm cấu hình nhánh main yêu cầu hai approve, nghĩa là cả hai thành
viên còn lại đều phải đồng ý thì MR mới được merge. Quy tắc này ngăn trường hợp một
người tự merge code chưa ai xem vào bản nộp cuối. Nhánh develop yêu cầu nhẹ hơn, chỉ
cần một approve để tốc độ làm bài không bị chậm.
Hình 11 tóm tắt luồng MR từ nhánh tính năng tới nhánh chính, nhấn mạnh hai chốt
chặn quan trọng là pipeline và số lượng approve.
Nhanh tinh nang Mo MR
Review va
Approve
Merge vao
main
push pipeline 2 approve
Hình 11: Luong Merge Request tu nhanh tinh nang toi nhanh chinh
Ví dụ dưới đây tạo MR bằng API rồi tạo Approval rule yêu cầu hai người phê duyệt.
Trong thực tế nhóm cấu hình bằng giao diện web, nhưng các lệnh này giúp hiểu rõ bản
chất và có thể dùng lại khi dựng Project mới cho môn học khác [8].
1 # Create a merge request from feature branch to main
2 curl -- request POST \
3 -- header " PRIVATE - TOKEN : $GITLAB_TOKEN " \
4 -- data " source_branch = feature / login - aspx " \
5 -- data " target_branch = main " \
6 -- data " title = Merge login form to main " \
7 " https :// gitlab . com / api / v4 / projects / $PROJECT_ID / merge_requests "
78

---

## [Page 80] (`page-80.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
8 # Require 2 approvals before merge ( approval rule )
9 curl -- request POST \
10 -- header " PRIVATE - TOKEN : $GITLAB_TOKEN " \
11 -- data " name = Require 2 approvers " \
12 -- data " approvals_required =2 " \
13 " https :// gitlab . com / api / v4 / projects / $PROJECT_ID / approval_rules "
Listing 29: Tạo Merge Request và Approval rule bằng API
5.4 Bảo vệ nhánh và tag
Bảo vệ nhánh là lớp khóa cuối cùng giữ cho các nhánh quan trọng không bị ghi đè trực
tiếp. GitLab phân biệt hai quyền riêng: Allowed to push quyết định ai được đẩy trực tiếp
lên nhánh, còn Allowed to merge quyết định ai được bấm nút merge MR vào nhánh đó.
Tách bạch hai quyền này giúp nhóm áp dụng quy tắc nghiêm cho bản nộp cuối, nhưng
vẫn linh hoạt cho nhánh phát triển hằng ngày [8].
Nhóm áp dụng cấu hình trong Bảng 15 cho hai nhánh quan trọng nhất.
Bảng 15: Cấu hình bảo vệ cho hai nhánh main và develop
Nhánh Allowed to push Allowed to merge Yêu cầu bổ sung
main Không ai Maintainers 2 approve, pipeline thành công
develop Developers Developers 1 approve, pipeline thành công
Với cấu hình trên, nhánh main không cho phép đẩy trực tiếp bằng lệnh git push, mọi
thay đổi bắt buộc phải qua MR và được hai người phê duyệt. Nhánh develop cho phép
thành viên đẩy trực tiếp khi sửa lỗi nhỏ, nhưng các tính năng lớn như thêm trang quản
trị vẫn phải mở MR để có người kiểm tra chéo. Cách phân quyền này cân bằng giữa an
toàn và tốc độ, rất phù hợp với nhóm ba người.
Ngoài nhánh, GitLab còn cho phép bảo vệ tag để khóa các mốc phát hành. Nhóm
gắn tag v1.0 cho bản nộp giữa kỳ và tag v2.0 cho bản nộp cuối, sau đó cấu hình chỉ
Maintainers mới được tạo tag, tránh việc gắn nhầm tag lên commit lỗi. Khi cần chấm lại
bản cũ, giảng viên chỉ cần checkout đúng tag là có đúng bản đã nộp.
Các lệnh dưới đây minh họa cách bảo vệ nhánh bằng API, tương đương với thao tác
trên giao diện web. Mức quyền số 0 nghĩa là không ai được đẩy trực tiếp, mức 30 là
Developers, mức 40 là Maintainers.
1 # Protect main : no direct push , only maintainers can merge
2 curl -- request POST \
3 -- header " PRIVATE - TOKEN : $GITLAB_TOKEN " \
4 -- data " name = main " \
79

---

## [Page 81] (`page-81.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
5 -- data " push_access_level =0 " \
6 -- data " merge_access_level =40 " \
7 " https :// gitlab . com / api / v4 / projects / $PROJECT_ID /
protected_branches "
8 # Protect develop : developers can push and merge with review
9 curl -- request POST \
10 -- header " PRIVATE - TOKEN : $GITLAB_TOKEN " \
11 -- data " name = develop " \
12 -- data " push_access_level =30 " \
13 -- data " merge_access_level =30 " \
14 " https :// gitlab . com / api / v4 / projects / $PROJECT_ID /
protected_branches "
Listing 30: Bảo vệ nhánh main và develop bằng API
Tóm lại, GitLab cung cấp cho nhóm đầy đủ công cụ cộng tác từ Group tới Snippets,
với Merge Request và Approval rules làm trung tâm kiểm soát chất lượng. Khi kết hợp
thêm bảo vệ nhánh và tag, nhóm ba sinh viên có thể làm việc song song mà không sợ
mất code hay ghi đè bản nộp cuối của nhau. Đây chính là nền tảng để chương tiếp theo
xây dựng pipeline CI/CD tự động cho đồ án ASPX 4.8.1.
5.5 Khái niệm pipeline: stages, jobs, artifacts, cache, needs và
rules
Trong GitLab, mỗi lần lập trình viên đẩy mã nguồn lên một nhánh, hoặc khi một merge
request được tạo ra hay cập nhật, GitLab CI/CD sẽ tự động kích hoạt một pipeline: một
luồng công việc gồm nhiều bước kiểm tra, biên dịch và triển khai chạy nối tiếp nhau.
Pipeline giúp nhóm phát hiện lỗi sớm, chuẩn hóa quy trình build và loại bỏ thao tác thủ
công dễ sai sót khi phát hành phiên bản mới cho dự án ASPX [7].
Một pipeline gồm sáu khái niệm cốt lõi mà sinh viên cần nắm vững trước khi viết tệp
cấu hình:
Stages là các giai đoạn lớn chạy tuần tự, ví dụ build rồi đến test rồi đến deploy. Một
stage chỉ bắt đầu khi mọi job của stage trước đã thành công.
Jobs là đơn vị công việc nhỏ nhất trong pipeline, ví dụ job biên dịch solution hay job
chạy kiểm thử. Các job cùng một stage sẽ chạy song song nếu có đủ runner rảnh.
Artifacts là các tệp kết quả mà job giữ lại sau khi chạy xong, ví dụ thư mục publish/
chứa website đã biên dịch, hoặc báo cáo kiểm thử định dạng JUnit. Các job ở stage
sau có thể tải artifacts của stage trước về để sử dụng tiếp.
80

---

## [Page 82] (`page-82.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Cache là cơ chế lưu trữ tạm giúp tăng tốc các lần chạy sau, ví dụ cache thư mục gói
NuGet đã tải. Khác với artifacts, cache không đảm bảo toàn vẹn và có thể bị xóa
bất cứ lúc nào.
Needs cho phép một job chạy ngay khi các job mà nó phụ thuộc hoàn thành, thay vì
chờ cả stage trước kết thúc. Nhờ needs, pipeline thực thi theo đồ thị có hướng nên
nhanh hơn.
Rules quyết định job có được tạo ra hay không dựa trên tên nhánh, tag hay loại sự kiện
kích hoạt. Ví dụ job triển khai production chỉ chạy khi nhánh là main.
Hình 12 minh họa pipeline ba giai đoạn điển hình cho dự án ASPX: mã nguồn sau khi
commit được build bằng MSBuild, kiểm thử bằng VSTest, rồi triển khai lên staging.
Commit Build Test Deploy
push msbuild vstest
Hình 12: Luồng pipeline ba giai đoạn cho dự án ASPX
5.6 Tệp cấu hình hoàn chỉnh cho dự án ASPX 4.8.1
Mọi pipeline của GitLab đều được khai báo trong tệp .gitlab-ci.yml đặt ở thư mục
gốc của repository. Liệt kê 31 là một tệp hoàn chỉnh, áp dụng trực tiếp cho solution
AspxDemo.sln gồm một project Web Forms và một project kiểm thử đơn vị. Ví dụ giả định
runner Windows dùng shell PowerShell là mặc định của executor shell trên Windows.
1 # Full GitLab CI pipeline for ASPX (. NET Framework 4.8.1)
2 # Requires a Windows runner with MSBuild , NuGet and VSTest
3 stages :
4 - build
5 - test
6 - deploy
7 variables :
8 BUILD_CONFIG : " Release "
9 SOLUTION : " AspxDemo .sln"
10 PUBLISH_DIR : " publish "
11 # Cache NuGet packages between pipelines on the same runner
12 cache :
13 key : "nuget - $CI_COMMIT_REF_SLUG "
14 paths :
15 - packages /
16 # Stage 1: restore packages and build the solution
17 build :
18 stage : build
81

---

## [Page 83] (`page-83.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
19 tags :
20 - windows
21 - msbuild
22 script :
23 - nuget restore $env : SOLUTION
24 - msbuild $env : SOLUTION / p : Configuration = $env : BUILD_CONFIG / p
: DeployOnBuild = true / p : PublishDir = $env : PUBLISH_DIR \
25 artifacts :
26 paths :
27 - publish /
28 expire_in : 1 week
29 # Stage 2: run unit tests with VSTest , reuse build artifacts
30 test :
31 stage : test
32 tags :
33 - windows
34 needs :
35 - job : build
36 artifacts : true
37 script :
38 - vstest . console . exe AspxDemo . Tests \ bin \ $env : BUILD_CONFIG \
AspxDemo . Tests . dll / Logger :" trx; LogFileName = results .trx "
39 artifacts :
40 when : always
41 reports :
42 junit : TestResults \ results . trx
43 paths :
44 - TestResults /
45 # Stage 3: deploy to staging , only on the main branch
46 deploy :
47 stage : deploy
48 tags :
49 - windows
50 needs :
51 - build
52 rules :
53 - if : $CI_COMMIT_BRANCH == " main "
54 when : on_success
55 - when : never
56 script :
57 - xcopy publish \\ staging - server \ wwwroot \ AspxDemo / E / Y
82

---

## [Page 84] (`page-84.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
58 environment :
59 name : staging
60 url : http :// staging . example . com
Listing 31: Tệp cấu hình GitLab CI đầy đủ cho ASPX 4.8.1
Ý nghĩa từng khối trong tệp cấu hình trên như sau:
1. Khối stages khai báo ba giai đoạn chạy tuần tự: biên dịch, kiểm thử rồi triển khai.
Thứ tự khai báo chính là thứ tự thực thi của pipeline.
2. Khối variables định nghĩa các biến dùng chung như cấu hình build và tên solution,
giúp đổi cấu hình một chỗ mà không phải sửa từng job. Khối cache giữ lại thư mục
gói NuGet để lần chạy sau không phải tải lại từ Internet.
3. Job build gắn hai tag windows và msbuild để GitLab chọn đúng runner có cài
MSBuild. Job chạy nuget restore rồi msbuild với tham số xuất bản ra thư mục
publish/, sau đó lưu thư mục này thành artifacts trong một tuần.
4. Job test dùng needs để chạy ngay khi job build xong và nhận đúng bộ artifacts
của nó. Kết quả VSTest khai báo ở mục reports:junit để GitLab hiển thị trên
giao diện merge request, kèm when: always để luôn lưu báo cáo kể cả khi có test
thất bại.
5. Job deploy dùng rules để chỉ chạy khi nhánh là main; mọi nhánh khác đều bị bỏ
qua nhờ dòng when: never. Lệnh xcopy chép website lên máy chủ staging, đồng
thời khối environment đăng ký môi trường để theo dõi lịch sử triển khai.
5.7 Runner: shared, specific, group và vai trò của tag
Runner là chương trình trung gian chạy trên một máy tính riêng, chịu trách nhiệm nhận
job từ GitLab, thực thi từng dòng trong mục script, rồi gửi kết quả và artifacts trả
về máy chủ. Bản thân GitLab chỉ điều phối pipeline, còn mọi lệnh build đều chạy trên
runner. GitLab phân runner thành ba loại theo phạm vi phục vụ, so sánh trong Bảng 16:
83

---

## [Page 85] (`page-85.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Bảng 16: So sánh ba loại runner trong GitLab
Loại Phạm vi phục
vụ
Người quản
lý
Khi nào nên dùng
Shared Mọi project
trên máy chủ
Quản trị viên
hệ thống
Đồ án môn học và bài
tập nhỏ, không cần
môi trường đặc biệt
Group Mọi project
trong một
group
Trưởng nhóm
hoặc quản trị
viên
Nhóm sinh viên dùng
chung một runner
riêng của nhóm
Specific Một project
duy nhất
Chủ project Project ASPX cần
runner Windows gắn
với đúng một reposi￾tory
Mỗi runner được gắn một danh sách tag mô tả năng lực, ví dụ windows, msbuild hay
aspx. Khi job khai báo mục tags, GitLab chỉ giao job cho runner có đầy đủ các tag tương
ứng; job không khai báo tag sẽ chạy trên bất kỳ runner rảnh nào. Liệt kê 32 đăng ký một
runner Windows mới trên máy build.
1 # Run on the Windows build machine as Administrator
2 gitlab - runner register -- url https :// gitlab . com -- token glpat -9
f8e7d6c5b4a3210 -- executor shell -- shell powershell -- tag - list
" windows , msbuild , aspx " -- description " aspx - win - builder -01 "
3 gitlab - runner install
4 gitlab - runner start
5 gitlab - runner verify
6 # After verify , the runner appears under Settings > CI / CD >
Runners
Listing 32: Đăng ký Windows runner cho dự án ASPX
Với dự án ASPX trên .NET Framework 4.8.1, nhóm bắt buộc phải dùng runner Win￾dows có cài MSBuild đầy đủ, vì .NET Framework chỉ chạy trên Windows còn Web Forms
không thể biên dịch bằng bộ công cụ đa nền tảng trên Linux [9]. Cụ thể, MSBuild cần các
assembly tham chiếu của .NET Framework, trình biên dịch trang .aspx và VSTest để chạy
kiểm thử; các thành phần này không có trên runner Linux dùng image ubuntu-latest.
Vì vậy mọi job trong Liệt kê 31 đều gắn tag windows để tránh bị điều nhầm sang runner
Linux.
84

---

## [Page 86] (`page-86.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
5.8 Biến CI/CD: masked, protected và cách đọc qua biến môi
trường
Pipeline thường cần những thông tin nhạy cảm như chuỗi kết nối cơ sở dữ liệu, mật khẩu
triển khai hay khóa ký bản phát hành. GitLab cho phép khai báo các giá trị này ở mục
Settings, CI/CD, Variables thay vì ghi trực tiếp vào tệp cấu hình, nhờ đó mã nguồn công
khai không bao giờ chứa bí mật thật.
Hai thuộc tính quan trọng nhất của biến CI/CD là:
Masked yêu cầu GitLab che giá trị biến trong nhật ký job, thay bằng chuỗi [MASKED].
Thuộc tính này phù hợp với mật khẩu và khóa bí mật, nhưng giá trị phải đủ dài và
không chứa ký tự xuống dòng thì GitLab mới che được.
Protected yêu cầu biến chỉ được truyền cho pipeline chạy trên nhánh hoặc tag được bảo
vệ, ví dụ nhánh main. Nhờ đó, merge request từ nhánh lạ không thể đánh cắp bí
mật triển khai bằng cách in biến ra nhật ký.
Trong tệp .gitlab-ci.yml, biến được đọc theo cú pháp của shell trên runner: Pow￾erShell dùng $env:TEN_BIEN, cmd dùng %TEN_BIEN%, còn Bash dùng $TEN_BIEN. Với mã
nguồn C# của trang ASPX, cách đơn giản nhất là đọc biến môi trường của tiến trình
đang chạy, đồng thời giữ phương án dự phòng đọc từ Web.config khi chạy trên máy lập
trình viên như trong Liệt kê 33.
1 // Read connection string from a CI / CD variable ,
2 // fallback to Web . config on developer machines
3 string conn = System . Environment . GetEnvironmentVariable ( " DB_CONN "
) ;
4 if ( string . IsNullOrEmpty ( conn ) )
5 {
6 conn = System . Configuration . ConfigurationManager
7 . ConnectionStrings [ " Default " ]. ConnectionString ;
8 }
9 using ( var db = new System . Data . SqlClient . SqlConnection ( conn ) )
10 {
11 db . Open () ;
12 // Run queries here with the opened connection
13 }
Listing 33: Đọc biến môi trường từ mã nguồn trang ASPX
Quy tắc an toàn mà nhóm cần tuân thủ: mọi bí mật đều nằm trong Variables với cả
hai cờ masked và protected, tệp Web.config trong repository chỉ chứa chuỗi kết nối giả
cho môi trường phát triển, và không ai được in toàn bộ biến môi trường ra nhật ký job.
85

---

## [Page 87] (`page-87.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
5.9 Môi trường triển khai và Review Apps
Khối environment trong mỗi job triển khai đăng ký một môi trường có tên và địa chỉ
truy cập, ví dụ staging cho kiểm thử nội bộ và production cho người dùng thật. GitLab
gom lịch sử triển khai của từng môi trường vào trang Environments, nơi nhóm xem được
commit nào đang chạy ở đâu.
Liệt kê 34 minh họa ba kiểu triển khai phổ biến: staging tự động mỗi khi nhánh main
có commit mới, production triển khai thủ công bằng nút bấm để có người kiểm soát cuối
cùng, và Review App tự động dựng một môi trường tạm cho từng merge request để người
review trải nghiệm trực tiếp thay đổi trên trình duyệt.
1 # Staging deploys automatically on every main commit
2 deploy_staging :
3 stage : deploy
4 tags :
5 - windows
6 rules :
7 - if : $CI_COMMIT_BRANCH == " main "
8 script :
9 - xcopy publish \\ staging - server \ wwwroot \ AspxDemo / E / Y
10 environment :
11 name : staging
12 url : http :// staging . example . com
13 # Production needs one manual approval before deploy
14 deploy_production :
15 stage : deploy
16 tags :
17 - windows
18 rules :
19 - if : $CI_COMMIT_BRANCH == " main "
20 when : manual
21 script :
22 - xcopy publish \\ prod - server \ wwwroot \ AspxDemo / E / Y
23 environment :
24 name : production
25 url : http :// shop . example . com
26 # Temporary Review App per merge request , removed after one day
27 review_app :
28 stage : deploy
29 rules :
30 - if : $CI_MERGE_REQUEST_ID
31 script :
86

---

## [Page 88] (`page-88.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
32 - echo Deploy review app for $CI_MERGE_REQUEST_ID
33 environment :
34 name : review / $CI_COMMIT_REF_SLUG
35 url : http :// $CI_ENVIRONMENT_SLUG . example . com
36 on_stop : stop_review_app
37 auto_stop_in : 1 day
38 # Manual job that stops the Review App above
39 stop_review_app :
40 stage : deploy
41 rules :
42 - if : $CI_MERGE_REQUEST_ID
43 when : manual
44 script :
45 - echo Stop review app
46 environment :
47 name : review / $CI_COMMIT_REF_SLUG
48 action : stop
Listing 34: Môi trường staging, production và Review App
Khi phiên bản mới gặp sự cố trên production, GitLab hỗ trợ rollback theo hai cách: mở
trang Environments và bấm triển khai lại trên bản ổn định gần nhất để chạy lại pipeline
cũ, hoặc revert commit gây lỗi trên nhánh main để pipeline tự động triển khai bản đã
sửa. Cả hai cách đều giữ lại đầy đủ lịch sử ai đã rollback và rollback về commit nào, giúp
nhóm truy vết sự cố thay vì triển khai thủ công không để lại dấu vết.
Tóm lại, pipeline GitLab mang lại cho đồ án ASPX một quy trình khép kín: mỗi
commit trên nhánh main đều được build, kiểm thử và triển khai tự động lên đúng môi
trường, mọi bí mật nằm trong biến CI/CD được che và bảo vệ, còn mỗi merge request
đều có Review App riêng để giảng viên và thành viên trong nhóm dùng thử trước khi
approve và merge.
5.10 Container Registry và Package Registry lưu trữ nội bộ
GitLab tích hợp sẵn Container Registry cho Docker image và Package Registry cho nhiều
định dạng gói như NuGet, npm và Maven, giúp nhóm không cần dựng thêm máy chủ lưu
trữ riêng [8]. Với đồ án ASPX trên .NET Framework 4.8.1, nhóm thường dùng hai kho
này theo hai mục đích khác nhau: một kho chứa image builder có công cụ biên dịch, một
kho chứa thư viện dùng chung của nhóm.
Khác với kho công cộng, mọi image và gói trong GitLab đều kế thừa quyền truy cập
của project và group. Thành viên có quyền Developer mới được đẩy gói mới, còn khách
ngoài nhóm không thể đọc image nội bộ. Cách phân quyền này phù hợp khi mã nguồn
đồ án để ở chế độ riêng tư nhưng pipeline vẫn phải tải phụ thuộc nhanh và ổn định.
87

---

## [Page 89] (`page-89.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Trong pipeline, GitLab cung cấp sẵn biến môi trường trỏ tới kho chứa như địa chỉ
registry, tên image và token truy cập tạm thời. Job biên dịch chỉ cần đăng nhập một lần
bằng token của pipeline là có thể đẩy image mới mà không cần tạo tài khoản phụ. Cách
làm này tránh lộ mật khẩu trong mã nguồn và chạy được trên cả máy chủ dùng chung
lẫn máy chủ tự quản.
• Container Registry: lưu image Windows có msbuild, công cụ NuGet và thư viện
nền cho Web Forms.
• Package Registry cho NuGet: xuất bản thư viện dùng chung như AspxDemo.Core
để các project tái sử dụng.
• Quyền đọc ghi kế thừa từ project, hỗ trợ token hết hạn nhanh cho từng pipeline.
• Chính sách dọn dẹp tự động giúp xóa image cũ, tránh đầy ổ đĩa trên máy chủ.
Ví dụ sau đăng nhập registry của chính project, đóng gói image builder rồi đẩy thư
viện NuGet nội bộ lên GitLab. Mọi chú thích trong khối lệnh đều viết không dấu theo
quy tắc của báo cáo.
1 # Login to the project registry with the CI token
2 docker login $CI_REGISTRY -u $CI_REGISTRY_USER -p
$CI_REGISTRY_PASSWORD
3 # Build the Windows builder image for ASPX 4.8.1
4 docker build -t $CI_REGISTRY_IMAGE / builder :4.8.1 -f Dockerfile .
windows .
5 docker push $CI_REGISTRY_IMAGE / builder :4.8.1
6 # Pack and push the shared NuGet library
7 nuget pack AspxDemo . Core . nuspec - Version 1.2.0 - OutputDirectory
out
8 nuget push out / AspxDemo . Core .1.2.0. nupkg - Source $NUGET_FEED_URL
- ApiKey $CI_JOB_TOKEN
Listing 35: Day image builder va goi NuGet noi bo
Với project ASPX 4.8.1, nhóm nên chốt một image builder duy nhất cho cả học kỳ,
ví dụ image chứa Visual Studio Build Tools và .NET Framework 4.8.1. Mọi job biên dịch
đều dùng lại image này nên kết quả build ổn định, tránh lỗi máy này chạy được còn máy
khác thì không. Thư viện dùng chung cũng nên đánh phiên bản tăng dần để khi có lỗi
chỉ cần quay về phiên bản cũ là chạy lại được [3].
5.11 Merge trains gộp nhiều Merge Request song song an toàn
Khi ba thành viên cùng mở Merge Request vào giờ chót, việc gộp tuần tự từng cái rất
chậm mà gộp ồ ạt thì dễ hỏng nhánh chính. Merge train giải quyết đúng bài toán này
88

---

## [Page 90] (`page-90.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
bằng cách xếp các Merge Request đã được duyệt thành một đoàn tàu theo thứ tự, rồi cho
pipeline chạy trên kết quả gộp của cả đoàn thay vì chạy riêng từng cái [8].
Nguyên tắc hoạt động gồm ba bước lặp lại: thêm Merge Request vào cuối tàu, chạy
pipeline trên mã nguồn đã gộp tất cả các toa, rồi tự động gộp theo thứ tự khi pipeline
xanh. Nếu toa đầu bị đỏ thì cả tàu dừng lại, toa lỗi bị tách ra để tác giả sửa, các toa còn
lại tiếp tục chạy mà không cần xếp hàng lại từ đầu. Nhờ đó nhánh chính luôn xanh dù
nhiều người gộp song song.
1. Tác giả hoàn thiện Merge Request, xin đủ lượt duyệt theo Approval rules rồi bấm
thêm vào tàu.
2. GitLab tạo pipeline cho toàn bộ nội dung đã gộp, bao gồm biên dịch msbuild và
chạy kiểm thử.
3. Khi pipeline xanh, GitLab gộp từng toa theo đúng thứ tự đã xếp, nhanh hơn nhiều
so với gộp tay từng cái.
4. Khi pipeline đỏ, toa lỗi bị loại khỏi tàu, các toa sau tự động chạy lại trên kết quả
mới.
Hình sau minh họa một đoàn tàu gồm ba Merge Request xếp hàng vào nhánh chính.
Thứ tự trong tàu chính là thứ tự gộp, vì vậy thành viên nên trao đổi trước để xếp phần
ít rủi ro lên đầu.
MR 1 MR 2 MR 3 main
toa 1 toa 2 gop
Hình 13: Doan tau gop gom ba MR xep hang vao nhanh main
Với đồ án môn học, Merge trains phát huy tác dụng nhất vào tuần nộp bài khi cả ba
nhánh tính năng cùng xin gộp. Nhóm nên bật thêm tùy chọn fast-forward only để lịch sử
nhánh chính luôn thẳng, kết hợp chính sách xóa nhánh nguồn sau khi gộp để danh sách
nhánh luôn gọn gàng [4].
5.12 Quét bảo mật tích hợp trong pipeline
GitLab tích hợp sẵn nhiều bộ quét bảo mật chạy ngay trong pipeline, giúp nhóm sinh
viên phát hiện lỗi sớm mà không cần cài thêm công cụ ngoài [7]. Chỉ cần khai báo đúng
tập tin mẫu là mỗi Merge Request đều được quét tự động, kết quả hiển thị ngay trong
trang Merge Request để người duyệt quyết định có cho gộp hay không.
89

---

## [Page 91] (`page-91.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Bảng 17: Bon loai quet bao mat pho bien nhat tren GitLab
Loại quét Phát hiện chính Thời điểm chạy Ghi chú cho ASPX
SAST Lỗi trong mã nguồn Mọi Merge Request Bật thêm quy tắc cho C#
Secret Detection Mật khẩu lộ trong mã Mọi commit mới Chặn connection string thật
Dependency Scanning Thư viện có lỗ hổng Pipeline hằng đêm Quét gói NuGet đã cài
Container Scanning Image có lỗ hổng Sau khi đóng gói Quét image builder
Trong bốn loại trên, Secret Detection là loại nhóm ASPX cần bật đầu tiên vì lỗi
phổ biến nhất là đẩy tập tin Web.config chứa connection string thật lên kho chung.
Dependency Scanning đứng thứ hai vì project Web Forms thường kéo theo nhiều gói
NuGet cũ. Hai loại còn lại giúp bảo vệ image builder và mã nguồn C# phía sau trang
ASPX.
Ví dụ sau bật ba bộ quét bằng cách kế thừa tập tin mẫu chính thức của GitLab. Cách
viết này ngắn gọn vì toàn bộ cấu hình chi tiết đã nằm sẵn trong mẫu, nhóm chỉ cần khai
báo thêm giai đoạn kiểm thử cho phù hợp với project của mình.
1 # Basic stages for an ASPX project with security scans
2 stages :
3 - test
4 - build
5 # Include the official GitLab security templates
6 include :
7 - template : Security / SAST . gitlab - ci . yml
8 - template : Security / Secret - Detection . gitlab - ci . yml
9 - template : Security / Dependency - Scanning . gitlab - ci . yml
10 # Force SAST to run on every merge request pipeline
11 sast :
12 stage : test
13 rules :
14 - if : $CI_PIPELINE_SOURCE == " merge_request_event "
Listing 36: Bat cac bo quet bao mat co ban
Khi bộ quét báo đỏ, nhóm không nên tắt quét để gộp cho nhanh mà nên đọc báo cáo,
sửa đúng chỗ rồi chạy lại pipeline. Với cảnh báo sai, GitLab cho phép đánh dấu bỏ qua
có ghi lý do, giúp buổi bảo vệ vẫn giải thích được vì sao nhóm quyết định như vậy thay
vì im lặng bỏ qua cảnh báo.
90

---

## [Page 92] (`page-92.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
5.13 Kiểm toán và tuân thủ với Audit Events
Mọi thao tác quan trọng trên GitLab như đổi quyền thành viên, sửa luật duyệt, gộp
Merge Request hay đổi biến môi trường của pipeline đều được ghi lại thành Audit Events
[8]. Mỗi sự kiện ghi rõ ai làm, làm gì, trên project nào và vào lúc nào, tạo thành nhật ký
không thể sửa giúp giảng viên và nhóm trưởng truy vết sau này.
Với quy trình ba người, nhật ký kiểm toán trả lời nhanh các câu hỏi thường gặp khi
có sự cố: ai đã gộp nhánh khi pipeline còn đỏ, ai đã xóa biến môi trường chứa connection
string, ai đã thêm người ngoài vào project. Nhờ có nhật ký, nhóm không cần đoán mà chỉ
cần lọc sự kiện theo tên người hoặc theo khoảng thời gian.
Ai tên tài khoản thực hiện thao tác, kèm địa chỉ IP khi đăng nhập qua giao diện web.
Việc gì hành động cụ thể như gộp Merge Request, đổi quyền hay sửa luật bảo vệ nhánh.
Ở đâu project hoặc group xảy ra sự kiện, kèm liên kết tới Merge Request liên quan.
Khi nào mốc thời gian đầy đủ giúp đối chiếu với lịch sử pipeline và lịch sử commit.
Ngoài nhật ký mặc định, GitLab còn hỗ trợ Compliance Frameworks cho các tổ chức
cần quy trình chặt chẽ, ví dụ bắt buộc mọi Merge Request vào nhánh phát hành phải
có đủ hai lượt duyệt và pipeline xanh. Với đồ án môn học, nhóm không cần bật toàn bộ
khung tuân thủ mà chỉ cần giữ ba thói quen: cấm đẩy thẳng nhánh chính, yêu cầu ít nhất
một lượt duyệt và xuất nhật ký kiểm toán khi nộp báo cáo.
Một mẹo nhỏ là gắn nhãn cho từng Merge Request theo loại công việc như tính năng,
sửa lỗi hay tài liệu. Khi lọc nhật ký theo nhãn, nhóm sẽ thống kê được mỗi thành viên
đã gộp bao nhiêu Merge Request thuộc loại nào, rất tiện cho phần tự đánh giá đóng góp
trong báo cáo và slide bảo vệ [1].
5.14 Tự host GitLab và sao lưu phục hồi
Bên cạnh bản dịch vụ đám mây, GitLab cho phép tự host toàn bộ hệ thống trên máy chủ
của khoa hoặc của nhóm, giúp chủ động về dữ liệu và đường truyền nội bộ [8]. Lựa chọn
này phù hợp khi đồ án chứa mã nguồn không được phép đưa lên dịch vụ công cộng, hoặc
khi phòng lab muốn sinh viên làm quen với quản trị hệ thống thật.
Yêu cầu phần cứng tối thiểu cho nhóm nhỏ khá vừa phải: máy chủ hai nhân, bộ nhớ
8 GB và ổ cứng trống khoảng 20 GB là đủ chạy ổn định cho dưới một trăm người dùng.
Với quy mô ba sinh viên, nhóm có thể cài bản Omnibus trên một máy ảo duy nhất, còn
bản mở rộng nhiều máy chỉ cần khi phục vụ toàn khoa với hàng nghìn pipeline mỗi ngày.
• Hệ điều hành Ubuntu 64 bit bản hỗ trợ dài hạn, đã mở cổng cho giao diện web và
kho Git.
91

---

## [Page 93] (`page-93.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
• Tối thiểu 2 CPU, RAM 8 GB, ổ cứng SSD trống 20 GB cho nhóm dưới 100 người
dùng.
• Tên miền nội bộ và chứng chỉ số để bật HTTPS, tránh trình duyệt báo kết nối
không an toàn.
• Máy chạy pipeline riêng cho Windows để biên dịch project ASPX 4.8.1 bằng msbuild.
Cài đặt xong chưa đủ, nhóm quản trị phải lên lịch sao lưu tự động vì mọi mã nguồn
và lịch sử Merge Request đều nằm trên máy chủ tự host. GitLab cung cấp sẵn lệnh sao
lưu tạo một gói duy nhất chứa cơ sở dữ liệu, kho Git và tập tin đính kèm, kèm lệnh khôi
phục để dựng lại hệ thống khi máy chủ gặp sự cố.
1 # Create a full backup package on the GitLab server
2 sudo gitlab - backup create
3 # List backup files and copy one copy to safe storage
4 ls / var / opt / gitlab / backups /
5 scp / var / opt / gitlab / backups / APP_BACKUP . tar user@backup - host :/ safe
/
6 # Stop services , restore , then restart and check health
7 sudo gitlab - ctl stop puma
8 sudo gitlab - ctl stop sidekiq
9 sudo gitlab - backup restore BACKUP = APP_BACKUP
10 sudo gitlab - ctl reconfigure
11 sudo gitlab - ctl restart
12 sudo gitlab - rake gitlab : check SANITIZE = true
Listing 37: Sao luu va khoi phuc GitLab tu host
Với đồ án môn học, nhóm nên sao lưu mỗi tuần một lần và giữ ít nhất hai bản gần
nhất ở máy khác. Trước buổi bảo vệ, hãy diễn tập khôi phục một lần trên máy ảo phụ để
chắc chắn bản sao lưu dùng được, tránh tình huống đến ngày nộp bài mới phát hiện tập
tin sao lưu bị lỗi [2].
5.15 Auto DevOps pipeline tự sinh cho dự án mới
Auto DevOps là bộ mẫu pipeline do GitLab xây dựng sẵn, có khả năng tự phát hiện loại
project rồi sinh ra đầy đủ các giai đoạn từ biên dịch, kiểm thử đến quét bảo mật và triển
khai [7]. Với nhóm mới học CI/CD, đây là cách nhanh nhất để có pipeline chạy xanh ngay
trong buổi đầu mà chưa cần viết nhiều cấu hình.
Luồng mặc định gồm các giai đoạn nối tiếp nhau: phát hiện ngôn ngữ, biên dịch và
kiểm thử, quét chất lượng và bảo mật, đóng gói image, rồi triển khai tới môi trường đánh
giá. Mỗi giai đoạn đều có thể tắt hoặc ghi đè khi nhóm đã đủ kiến thức tự viết job riêng,
vì vậy Auto DevOps vừa là điểm khởi đầu vừa là tài liệu mẫu để học.
92

---

## [Page 94] (`page-94.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
1. Bật Auto DevOps trong phần cài đặt CI/CD của project rồi đẩy một commit mới.
2. GitLab tự phát hiện project, sinh pipeline và chạy thử toàn bộ các giai đoạn mặc
định.
3. Nhóm đọc kết quả từng job, giữ lại giai đoạn phù hợp và tắt giai đoạn chưa cần.
4. Khi đã tự tin, nhóm chép các job mẫu ra tập tin riêng rồi tùy biến cho ASPX 4.8.1.
Cần lưu ý rằng mẫu mặc định tối ưu cho project hiện đại dùng container trên Linux,
trong khi project ASPX 4.8.1 cần máy chạy Windows và lệnh msbuild [9]. Vì vậy nhóm
Web Forms nên coi Auto DevOps là bản nháp tham khảo: học cách chia giai đoạn và cách
bật quét bảo mật từ mẫu, sau đó viết pipeline riêng với nhãn máy chạy Windows cho các
job biên dịch thật [10].
Một cách tiếp cận khôn ngoan là bật Auto DevOps trên một project thử nghiệm song
song với project đồ án chính. Mọi thử nghiệm cấu hình đều thực hiện bên project thử,
khi nào chạy ổn mới chép sang project chính. Cách làm này giữ cho pipeline của đồ án
luôn xanh trong suốt học kỳ.
5.16 Các gói Free, Premium, Ultimate và gợi ý cho đồ án môn
học
GitLab cung cấp ba gói chính với cùng một nền tảng nhưng khác nhau về tính năng quản
lý và bảo mật [8]. Gói Free đủ cho hầu hết đồ án môn học, trong khi hai gói trả phí phù
hợp với đồ án tốt nghiệp có yêu cầu cao hơn hoặc với doanh nghiệp triển khai thật.
Bảng 18: So sanh nhanh ba goi GitLab cho nhom sinh vien
Tính năng Free Premium Ultimate
Kho riêng tư và Merge Request Có Có Có
Pipeline CI/CD cơ bản Có Có Có
Approval rules nâng cao Giới hạn Có Có
Merge trains Không Có Có
Quản lý môi trường triển khai Có Có Có
SAST và Secret Detection Có Có Có
Dependency và Container Scanning Cơ bản Đầy đủ Đầy đủ
Audit Events chi tiết Cơ bản Đầy đủ Đầy đủ
Với nhóm ba sinh viên làm project ASPX 4.8.1, gói Free đã đáp ứng toàn bộ yêu
cầu bắt buộc: kho riêng tư, Merge Request có duyệt, pipeline biên dịch trên máy chạy
Windows và hai bộ quét bảo mật cơ bản. Nhóm chỉ cần tự bù lại hai thiếu sót là Merge
93

---

## [Page 95] (`page-95.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
trains và luật duyệt nâng cao bằng cách phân công một người chịu trách nhiệm gộp cuối
cùng vào ngày nộp bài.
Khi cần trình bày phần mở rộng trong buổi bảo vệ, nhóm có thể nêu rõ nếu nâng lên
Premium thì quy trình gộp sẽ an toàn hơn nhờ Merge trains, còn Ultimate bổ sung thêm
bảng điều khiển bảo mật tổng hợp cho toàn bộ group. Cách trình bày này cho thấy nhóm
hiểu rõ giới hạn của gói miễn phí và biết khi nào nên nâng cấp thay vì đòi hỏi bản quyền
tốn kém ngay từ đầu [5].
Tóm lại, chương này đã đi qua bảy mảnh ghép nâng cao của GitLab từ kho chứa,
đoàn tàu gộp, quét bảo mật, kiểm toán, tự host, pipeline tự sinh đến các gói dịch vụ.
Nắm vững bảy nội dung này, nhóm có thể vận hành trọn vẹn một quy trình phát triển
ASPX 4.8.1 theo đúng chuẩn công nghiệp: mọi thay đổi đều qua Merge Request, mọi bản
gộp đều có pipeline xanh và nhật ký rõ ràng.
6 So sánh Git, GitHub và GitLab
Nhiều bạn mới học thường gọi gộp cả ba cái tên Git, GitHub và GitLab thành một chữ
git cho gọn. Cách gọi này gây nhầm lẫn khi làm đồ án, vì Git là công cụ chạy trên máy
cá nhân, còn GitHub và GitLab là dịch vụ máy chủ dùng để cộng tác nhóm [2, 1]. Chương
này làm rõ sự khác nhau giữa ba khái niệm, so sánh chi tiết GitHub với GitLab trên hơn
hai mươi tiêu chí, đối chiếu các tính năng tương đương, rồi đưa ra khuyến nghị cụ thể
cho đồ án môn học ASPX trên .NET Framework 4.8.1 [10].
6.1 Git, GitHub và GitLab khác nhau thế nào
Git là hệ thống quản lý phiên bản phân tán, nghĩa là mỗi máy giữ đầy đủ lịch sử commit
và làm việc offline hoàn toàn với các lệnh như git add, git commit, git branch hay
git log [2]. GitHub và GitLab là hai nền tảng trực tuyến xây dựng quanh Git, bổ sung
kho chứa tập trung, quản lý công việc, review code và CI/CD [6, 8]. Nói ngắn gọn: Git là
cái búa miễn phí ai cũng cầm được, còn GitHub và GitLab là hai xưởng mộc cùng dùng
loại búa đó nhưng cách tổ chức khác nhau. Bảng 19 tóm tắt sự khác nhau cốt lõi giữa ba
khái niệm này.
94

---

## [Page 96] (`page-96.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Bảng 19: Khác nhau cốt lõi giữa Git, GitHub và GitLab
Tiêu chí Git GitHub GitLab
Bản chất Hệ thống quản lý
phiên bản phân tán
[2]
Nền tảng hosting và
cộng tác dựa trên
Git [6]
Nền tảng DevOps
tích hợp dựa trên
Git [8]
Chạy ở đâu Máy cá nhân của
từng thành viên
Đám mây GitHub,
hoặc máy chủ riêng
bản Enterprise
Đám mây Git￾Lab.com, hoặc máy
chủ riêng miễn phí
Cần mạng
không
Không cần cho com￾mit, nhánh, xem log;
chỉ cần khi push và
pull
Cần mạng cho hầu
hết thao tác cộng tác
Cần mạng cho hầu
hết thao tác cộng tác
Ví dụ thao
tác
git commit,
git merge
Tạo PR, review
code, chạy Actions
Tạo MR, approve,
chạy pipeline
Chi phí Miễn phí, mã nguồn
mở
Gói Free, Team, En￾terprise
Gói Free, Premium,
Ultimate, bản tự
quản miễn phí
Đoạn lệnh 38 cho thấy Git local chạy offline hoàn toàn, chỉ khi đẩy code lên GitHub
hoặc GitLab mới cần kết nối mạng.
1 # 1. Lam viec offline hoan toan tren may ca nhan
2 git init AspxDemo_NET481
3 cd AspxDemo_NET481
4 git add .
5 git commit -m " feat : khoi tao project ASPX 4.8.1 "
6 git log -- oneline
7 git branch feature / login
8 git switch feature / login
9 # 2. Can mang Internet khi day code len server
10 git remote add origin https :// github . com / nhom3 / AspxDemo_NET481 .
git
11 git push -u origin feature / login
Listing 38: Git local lam viec offline, day len remote moi can mang
Hình 14 minh họa mô hình nhóm 3 người dùng trong đồ án: mỗi máy chạy Git local,
cùng đẩy code lên hai remote là GitHub và GitLab.
95

---

## [Page 97] (`page-97.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Git local
may sinh vien
GitHub
remote chinh
GitLab
remote mirror
push/pull
push/mirror
Hình 14: Mỗi máy chạy Git local và đẩy code lên GitHub và GitLab
Điểm mấu chốt cần nhớ: thành thạo Git local là nền tảng bắt buộc của mọi thành
viên, còn GitHub hay GitLab chỉ là nơi đặt kho remote và bộ công cụ cộng tác phía trên.
Mất mạng vẫn commit, tạo nhánh và xem lịch sử bình thường, đó chính là sức mạnh của
mô hình phân tán.
6.2 So sánh chi tiết GitHub và GitLab trên hơn hai mươi tiêu
chí
GitHub và GitLab trùng nhau khoảng 80% chức năng phổ biến như lưu trữ code, theo dõi
công việc và review, nhưng khác nhau rõ ở triết lý: GitHub mạnh về cộng đồng mã nguồn
mở và hệ sinh thái mở rộng, GitLab mạnh về quy trình DevOps khép kín và khả năng tự
quản máy chủ. Hai bảng dưới đây so sánh 22 tiêu chí, nhóm theo nền tảng, CI/CD, cộng
tác, bảo mật và chi phí để tiện đối chiếu khi chọn công cụ cho đồ án.
96

---

## [Page 98] (`page-98.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Bảng 20: So sánh GitHub và GitLab, phần 1: nền tảng, CI/CD và cộng tác
Tiêu chí GitHub GitLab
Bản chất nền
tảng
Hosting và cộng tác, mạnh
cộng đồng mở [6]
DevOps tích hợp một cửa,
mạnh tự quản [8]
Cài đặt self-host Khó: chỉ bản Enterprise
Server, tốn phí và cấu hình
nặng
Dễ: bản Community miễn phí,
cài một gói Omnibus
CI/CD tích hợp GitHub Actions, workflow
chạy theo sự kiện [5]
GitLab CI/CD, pipeline theo
stages minh bạch [7]
Runner Windows Có sẵn image windows-latest,
dùng ngay
Tự đăng ký Windows runner,
gắn nhãn windows
Build ASPX 4.8.1 Gọi msbuild trên windows￾latest, cache NuGet [9]
Gọi msbuild trên Windows
runner, cache tương tự
Review code Pull request, suggestion, re￾view theo từng file
Merge request, suggestion, re￾view đa cấp
Approval bắt
buộc
Rulesets và required review￾ers, bản trả phí đầy đủ hơn
Approval rules miễn phí đã
khá mạnh
Bảo vệ nhánh
main
Protected branch, status
check, CODEOWNERS
Protected branch, protected
tag, push rules
Quản lý công việc Issues và Projects dạng kan￾ban
Issues, Boards, Epics và Mile￾stones
Wiki và tài liệu Wiki, Pages và Discussions Wiki, Pages và Snippets
Package NuGet GitHub Packages hỗ trợ
NuGet, npm, Maven
Package Registry hỗ trợ
NuGet và Generic
97

---

## [Page 99] (`page-99.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Bảng 21: So sánh GitHub và GitLab, phần 2: bảo mật, chi phí và phù hợp ASPX
Tiêu chí GitHub GitLab
Container reg￾istry
Registry ghcr.io gắn với tài
khoản và tổ chức
Registry tích hợp sẵn trong
từng project
Trang tĩnh demo GitHub Pages, deploy từ
nhánh hoặc Actions
GitLab Pages, deploy qua job
trong pipeline
Quét secret lộ lọt Secret scanning và push pro￾tection
Secret detection chạy trong
pipeline
Quét bảo mật
code
Dependabot và CodeQL [6] SAST, DAST và Dependency
scanning [8]
Trợ lý AI Copilot gợi ý code trực tiếp
trong IDE
Duo gợi ý code và tóm tắt MR
Kho mở rộng Marketplace rất lớn, hàng
nghìn Actions sẵn
Tích hợp sẵn nhiều, chợ mở
rộng nhỏ hơn
Giới hạn gói free Khoảng 2000 phút Actions
mỗi tháng, 500 MB packages
Khoảng 400 phút CI mỗi
tháng, 5 GB registry
Giá gói trả phí Team khoảng 4 USD mỗi
người mỗi tháng
Premium khoảng 29 USD mỗi
người mỗi tháng
Mirror và import Nhập từ GitLab và Bitbucket,
mirror hạn chế
Mirror push và pull mạnh,
nhập từ GitHub dễ
Cộng đồng, việc
làm
Rất phổ biến, nhà tuyển dụng
hay xem profile
Phổ biến trong doanh nghiệp
tự quản máy chủ
Phù hợp đồ án
ASPX
Rất tốt: Actions Windows
sẵn, dễ demo pipeline xanh
Rất tốt: pipeline minh bạch,
hợp học DevOps
Con số giới hạn và giá ở hai bảng trên thay đổi theo chính sách hãng3
, nhưng thứ
tự lớn nhỏ tương đối giữ nguyên trong nhiều năm: GitHub hào phóng phút CI miễn phí
hơn, GitLab hào phóng tính năng DevOps miễn phí hơn. Với project ASPX 4.8.1 viết
bằng C# và Web Forms, cả hai nền tảng đều build được vì đều hỗ trợ runner Windows
gọi msbuild [9]. Khác biệt thực tế nằm ở trải nghiệm: Actions cấu hình nhanh trong vài
phút, còn pipeline GitLab mô tả stages rõ ràng nên dễ trình bày trước lớp hơn.
6.3 Các tính năng tương đương giữa hai nền tảng
Sinh viên đã quen một nền tảng có thể chuyển sang nền tảng còn lại rất nhanh vì hầu
hết tính năng đều có cặp tương đương, chỉ khác tên gọi và chút ít thao tác. Bảng 22 liệt
3Cần kiểm tra bảng giá chính thức trước ngày bảo vệ: https://github.com/pricing và https:
//about.gitlab.com/pricing.
98

---

## [Page 100] (`page-100.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
kê 8 cặp tương đương hay dùng nhất trong đồ án, kèm ghi chú để khi thầy cô hỏi phản
biện có thể trả lời ngay.
Bảng 22: Tám cặp tính năng tương đương giữa GitHub và GitLab
Nhu cầu GitHub GitLab
Đề xuất hợp nhất
code
Pull request, gọi tắt PR Merge request, gọi tắt MR
Tích hợp CI/CD Actions với file YAML trong
workflows
Pipelines với file
.gitlab-ci.yml
Soạn code trên
web
Codespaces chạy VS Code
trên đám mây
Web IDE gọn nhẹ kèm termi￾nal
Quản lý công việc Issues và Projects Issues và Boards
Chứa gói NuGet GitHub Packages Package Registry
Trang web tĩnh
demo
GitHub Pages GitLab Pages
Quét bảo mật tự
động
Dependabot và CodeQL SAST và Dependency scan￾ning
Trợ lý AI gợi ý
code
Copilot Duo
Điểm khác tên dễ gây lú nhất là PR và MR: Pull request của GitHub và Merge request
của GitLab thực chất cùng một việc là xin hợp nhất nhánh có review, chỉ khác tên vì lịch
sử hai hãng [6, 8]. Tương tự, Actions và Pipelines cùng mô tả các bước build, test, deploy
bằng YAML, nên đã viết được file YAML cho bên này thì đọc hiểu file YAML bên kia
trong vài phút. Đoạn lệnh 39 cho thấy cách gắn cả hai remote vào một repo local để đẩy
code song song, đây là bước chuẩn bị cho mô hình mirror ở mục sau.
1 # Gan 2 remote : GitHub lam chinh , GitLab lam mirror
2 git remote add github https :// github . com / nhom3 / AspxDemo_NET481 .
git
3 git remote add gitlab https :// gitlab . com / nhom3 / AspxDemo_NET481 .
git
4 git remote -v
5 # Day mot nhanh len ca hai noi
6 git push github main
7 git push gitlab main
8 # Mirror tu dong : tren GitLab vao Settings -> Repository ->
Mirroring ,
9 # dan URL repo GitHub , che do Push , pipeline chay khi co commit
moi
99

---

## [Page 101] (`page-101.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Listing 39: Gan ca hai remote GitHub va GitLab vao mot repo
6.4 Khuyến nghị cho đồ án môn học ASPX
Không có đáp án đúng duy nhất cho mọi nhóm, vì lựa chọn phụ thuộc vào mục tiêu demo,
thời gian và máy móc sẵn có. Phần này đưa ra ba khuyến nghị cụ thể: khi nào nên chọn
GitHub, khi nào nên chọn GitLab, và vì sao nhóm 3 người quyết định dùng cả hai qua
cơ chế mirror.
6.4.1 Khi nào nên chọn GitHub
• Muốn demo nhanh trong 5 đến 7 phút: tạo repo, bật Actions với image Windows
sẵn, pipeline build msbuild xanh ngay mà không cần cài runner riêng [5, 9].
• Nhóm có thành viên mới học Git: tài liệu, video hướng dẫn và câu trả lời trên mạng
cho GitHub nhiều nhất, tra cứu lỗi nhanh hơn hẳn.
• Muốn khoe profile khi xin thực tập: nhà tuyển dụng quen xem hồ sơ GitHub, số
PR và mảng contribution xanh là điểm cộng trực quan.
• Cần trang demo tĩnh gấp: GitHub Pages xuất bản slide hoặc tài liệu nhóm chỉ bằng
vài cú nhấp chuột từ nhánh chính.
6.4.2 Khi nào nên chọn GitLab
• Muốn học DevOps bài bản: pipeline stages, environments và review apps thể hiện
trực quan tư duy tích hợp và triển khai liên tục [7].
• Cần approval chặt mà không tốn phí: approval rules và protected branch của GitLab
ở gói miễn phí đã đủ để demo quy trình review nghiêm túc trước lớp.
• Phòng lab cho phép tự quản máy chủ: bản Community cài trên một máy tính của
khoa là cả lớp có forge riêng để thực hành mà không phụ thuộc mạng quốc tế.
• Muốn một nơi làm tất cả: issues, MR, CI/CD, registry và Pages nằm chung một
project, đỡ phải mở nhiều dịch vụ rời rạc.
6.4.3 Vì sao nhóm dùng cả hai qua cơ chế mirror
Nhóm 3 người quyết định lấy GitHub làm kho chính vì Actions Windows cấu hình nhanh,
đồng thời mirror sang GitLab để tận dụng pipeline stages minh bạch khi thuyết trình.
Mỗi thành viên làm trên nhánh feature riêng, mở PR bên GitHub để review, code sau khi
100

---

## [Page 102] (`page-102.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
merge tự động mirror sang GitLab và kích hoạt pipeline đối chứng. Cách làm này cho ba
lợi ích rõ rệt: thứ nhất, cả nhóm thực hành được cả PR lẫn MR nên trả lời tốt mọi câu
hỏi phản biện; thứ hai, bảng so sánh trong báo cáo có số liệu thật đo từ hai pipeline chạy
cùng một commit; thứ ba, luôn có một bản sao dự phòng khi một trong hai dịch vụ nghẽn
mạng đúng hôm demo. Đoạn lệnh 40 là khung pipeline GitLab tối thiểu mà nhóm dùng
cho project ASPX, chạy trên Windows runner và gọi msbuild giống hệt job bên GitHub
Actions.
1 # .gitlab -ci.yml skeleton for ASPX 4.8.1 on Windows runner
2 stages :
3 - build
4 - test
5 variables :
6 BUILD_CONFIG : ’Release ’
7 build - aspx :
8 stage : build
9 tags :
10 - windows
11 script :
12 - nuget restore AspxDemo . sln
13 - msbuild AspxDemo . sln / p : Configuration = Release
14 artifacts :
15 paths :
16 - AspxDemo / bin / Release /
17 test - aspx :
18 stage : test
19 tags :
20 - windows
21 script :
22 - vstest . console . exe AspxDemo . Tests / bin / Release / AspxDemo .
Tests . dll
23 dependencies :
24 - build - aspx
Listing 40: Khung pipeline GitLab toi thieu build ASPX 4.8.1
Quy trình nhánh của nhóm tuân theo GitFlow thu gọn [4]: nhánh main luôn build
xanh, nhánh develop gom tính năng, mỗi tính năng một nhánh feature ngắn ngày rồi
merge qua PR hoặc MR. Mọi commit tuân thủ Conventional Commits [3] với tiền tố như
feat, fix, docs, nhờ đó lịch sử đọc như nhật ký dự án thay vì mớ ghi chú lộn xộn. Tóm
lại, GitHub phù hợp khi cần nhanh và khoe được thành quả, GitLab phù hợp khi cần sâu
và trình bày được quy trình, còn dùng cả hai qua mirror là lựa chọn tối ưu cho bài trình
bày so sánh này.
101

---

## [Page 103] (`page-103.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
7 Áp dụng vào học phần ASPX
Chương này trình bày cách vận dụng Git, GitHub và GitLab vào đồ án môn học ASP.NET
Web Forms trên .NET Framework 4.8.1 cho nhóm 3 sinh viên [2, 6, 8, 10]. Khác với các
chương trước tập trung vào từng công cụ, chương này gom mọi kiến thức thành một quy
trình làm việc chung: tổ chức vai trò, mô hình nhánh, quy trình pull request và merge
request, checklist review, xử lý xung đột, quản lý secret và mẫu lịch sử commit. Mọi ví dụ
đều gắn với project Web Forms thật: file Web.config, trang Default.aspx, code behind
Default.aspx.cs viết bằng C# và build bằng msbuild [9]. Nhóm đọc xong chương này
có thể bắt tay làm đồ án ngay mà không cần thống nhất lại quy ước làm việc.
7.1 Tổ chức nhóm 3 người và mô hình nhánh
Nhóm 3 thành viên phân vai theo mảng trong file phân công: TV1 phụ trách Git local và
repo demo, TV2 phụ trách GitHub và GitHub Actions, TV3 phụ trách GitLab, so sánh
và tổng hợp báo cáo. Mỗi người vẫn phải biết đầy đủ quy trình chung, vai trò chỉ xác
định người chịu trách nhiệm chính khi có sự cố. Quy tắc quan trọng nhất: không ai được
push trực tiếp lên nhánh main, mọi thay đổi đều đi qua nhánh tính năng và pull request
hoặc merge request có ít nhất một người review [1, 6, 8].
• TV1 – Git và repo demo: tạo repo AspxDemo-NET481, viết file .gitignore chuẩn
ASP.NET, dựng lịch sử commit mẫu, chịu trách nhiệm giải quyết xung đột local và
kiểm tra mọi lệnh trong báo cáo chạy được.
• TV2 – GitHub và CI: quản trị repo GitHub, cấu hình protected branch và secret,
viết workflow ci-aspx-481.yml, đảm bảo mỗi pull request đều có pipeline build
xanh trước khi merge [5].
• TV3 – GitLab và tổng hợp: mirror repo sang GitLab, viết file .gitlab-ci.yml
cho Windows runner, cấu hình approval rule, vẽ bảng so sánh và tổng hợp báo cáo
[7].
Mô hình nhánh áp dụng GitFlow rút gọn với 3 tầng [4]:
• Nhánh main: luôn build được và deploy được, chỉ merge từ develop khi release,
mỗi commit trên main gắn thẻ git tag như v1.0.
• Nhánh develop: nhánh tích hợp hàng ngày, mọi nhánh tính năng đều tách từ đây
và merge ngược về đây qua pull request.
• Nhánh feature: tên theo mẫu feature/ten-tinh-nang, ví dụ feature/login-aspx
do TV1 làm, feature/github-actions do TV2 làm, feature/gitlab-ci do TV3
làm, xóa ngay sau khi merge.
102

---

## [Page 104] (`page-104.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
feature/* develop main
PR/MR + review release
Hình 15: Mô hình nhánh cho nhóm 3 người từ feature về develop rồi release lên main
Hình 15 tóm tắt luồng đi chuẩn: code trên nhánh feature, hợp nhất về develop qua
review, rồi mới release lên main. Nhánh main và develop đều được bảo vệ: chặn push
trực tiếp, yêu cầu ít nhất một approve và yêu cầu pipeline build xanh [6, 8]. Khi có lỗi
khẩn cấp trên bản release, tách nhánh hotfix/ten-loi từ main, sửa xong merge vào cả
main và develop để hai nhánh không lệch nhau. Cuối mỗi buổi làm việc, mọi người push
nhánh của mình lên remote để đồng đội thấy tiến độ, kể cả khi chưa mở pull request.
7.2 Quy trình pull request và merge request sáu bước
Mọi thay đổi code đều phải đi qua đúng 6 bước sau, áp dụng giống nhau cho pull request
trên GitHub và merge request trên GitLab. Quy trình này ngăn code lỗi lọt vào nhánh
chung và buộc mọi dòng code đều có ít nhất 2 cặp mắt kiểm tra.
1. Push nhánh tính năng lên remote: commit gọn theo Conventional Commits rồi
push bằng git push -u origin kèm tên nhánh, ví dụ feature/login-aspx.
2. Mở pull request về develop: mô tả rõ thay đổi gì, vì sao thay đổi, cách kiểm
thử, đính kèm ảnh chụp trang ASPX nếu có thay đổi giao diện.
3. Gán reviewer: mỗi pull request gán ít nhất một đồng đội làm reviewer, người còn
lại có thể subscribe để theo dõi, tuyệt đối không tự approve code của mình.
4. Chờ CI chạy xanh: pipeline tự động restore NuGet, build bằng msbuild và chạy
test, reviewer chỉ bắt đầu review khi pipeline đã xanh [5, 7, 9].
5. Review và approve: reviewer đi theo checklist ở mục sau, comment cụ thể từng
dòng, tác giả sửa rồi push thêm commit, reviewer approve khi hết ý kiến.
6. Merge và xóa nhánh: dùng merge commit để giữ lịch sử rõ ràng, merge xong xóa
nhánh feature trên remote để danh sách nhánh luôn gọn, pull develop mới về máy
local.
1 # TV1 : tao nhanh tinh nang tu develop moi nhat
2 git checkout develop
3 git pull origin develop
4 git checkout -b feature /login - aspx
5 # ... code tren Default . aspx va Default . aspx . cs ...
6 git add Default . aspx Default . aspx . cs Web . config
103

---

## [Page 105] (`page-105.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
7 git commit -m " feat : them form dang nhap voi validation server -
side "
8 git push -u origin feature /login - aspx
9 # mo pull request ve develop , gan TV2 lam reviewer
10 gh pr create -- base develop -- head feature /login - aspx \
11 -- title " feat : form dang nhap " \
12 -- reviewer TV2
Listing 41: Day nhanh tinh nang va mo pull request ve develop
Khối lệnh trên minh họa bước 1 và bước 2 cho TV1, các bước còn lại thực hiện trên
giao diện web GitHub hoặc GitLab. Nếu pipeline báo đỏ, tác giả phải sửa ngay, không
được nhờ reviewer bỏ qua và merge cố. Khi reviewer yêu cầu thay đổi, tác giả push thêm
commit mới thay vì sửa commit cũ, để reviewer thấy rõ phần nào đã sửa theo góp ý.
Merge xong, tác giả kiểm tra lại nhánh develop trên remote đã có code của mình rồi mới
xóa nhánh local bằng git branch -d.
7.3 Danh sách kiểm tra review code Web Forms
Reviewer dùng checklist 10 mục sau cho mọi pull request chạm vào code Web Forms,
thiếu một mục là chưa đủ điều kiện approve. Checklist này được đúc kết từ lỗi sinh viên
hay mắc khi làm đồ án ASPX với C# [10, 6].
1. Chống SQL injection: mọi câu lệnh SQL đều dùng tham số SqlParameter, cấm
nối chuỗi từ ô nhập liệu vào câu lệnh, kiểm tra kỹ các trang tìm kiếm và đăng nhập.
2. Chống XSS: dữ liệu người dùng hiển thị ra trang phải được encode bằng HttpUtility.HtmlEncode,
giữ nguyên cơ chế ValidateRequest, không tắt kiểm tra request khi chưa hiểu rõ.
3. Bảo vệ ViewState: bật MAC kiểm toàn vẹn ViewState, mã hóa ViewState khi
trang chứa dữ liệu nhạy cảm, không lưu mật khẩu hay quyền hạn vào ViewState
hay hidden field.
4. Validation hai lớp: mọi ràng buộc đều kiểm tra lại ở server bằng validator hoặc
code C# trong sự kiện, validation phía client chỉ để trải nghiệm mượt hơn chứ không
thay thế kiểm tra server.
5. File Web.config an toàn: thẻ biên dịch tắt debug ở bản release, customErrors
bật chế độ hiển thị trang lỗi thân thiện, không để lộ stack trace cho người dùng
cuối.
6. Connection string mẫu: file Web.config commit lên repo chỉ chứa connection
string mẫu trỏ về máy local, connection string thật của server lấy từ transform hoặc
secret của CI.
104

---

## [Page 106] (`page-106.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
7. Phân quyền: trang quản trị kiểm tra đăng nhập và vai trò trong sự kiện tải trang,
ẩn menu chưa đủ mà phải chặn cả khi người dùng gõ trực tiếp địa chỉ URL.
8. Xử lý lỗi và ghi log: khối truy vấn dữ liệu có xử lý ngoại lệ, lỗi ghi vào log hoặc
bảng log thay vì hiện chi tiết cho người dùng, đóng connection trong khối using.
9. Hiệu năng: tắt ViewState ở các control chỉ hiển thị như GridView danh sách lớn,
truy vấn có phân trang ở database thay vì tải toàn bộ bảng lên bộ nhớ.
10. Phong cách code: tên biến và hàm C# theo quy ước chung của nhóm, xóa code
thừa và dòng comment không còn đúng, message commit tuân thủ Conventional
Commits [3].
Khi phát hiện lỗi, reviewer comment đúng dòng code, giải thích vì sao sai và gợi ý
cách sửa, tránh comment chung chung kiểu code chưa ổn. Lỗi thuộc mục 1, 2, 5, 6 được
tính là lỗi nghiêm trọng: bắt buộc sửa trước khi merge, không được hẹn sang pull request
sau. Tác giả trả lời từng comment bằng cách sửa code hoặc giải thích lý do giữ nguyên,
sau đó yêu cầu review lại.
7.4 Xử lý xung đột file Web.config
File Web.config là nơi xung đột nhiều nhất vì cả 3 thành viên đều chạm vào: người thêm
connection string, người thêm cấu hình globalization, người bật tắt debug. Quy trình
chuẩn gồm 5 bước: lấy develop mới nhất, merge vào nhánh của mình, sửa marker xung
đột, build thử, rồi mới commit và push.
1 # dang o nhanh feature , lay develop moi nhat ve
2 git fetch origin
3 git merge origin / develop
4 # mo Web . config , tim cac cum marker xung dot
5 # giu ban mau , xoa marker , roi danh dau da xong
6 git add Web . config
7 git commit -m " fix : giai quyet conflict Web . config , giu
connection string mau "
8 # build thu truoc khi push
9 msbuild AspxDemo . sln / p : Configuration = Release
10 git push origin feature /login - aspx
Listing 42: Lay develop moi nhat va giai quyet xung dot Webconfig
Sau lệnh merge, Git chèn các cụm marker vào những đoạn hai bên cùng sửa, nhiệm vụ
của người sửa là đọc kỹ cả hai phía rồi viết lại thành một bản đúng duy nhất. Nguyên tắc
giữ code: giữ connection string mẫu trỏ về máy local, giữ mọi thẻ cấu hình mới của cả hai
bên, chỉ bỏ phần marker và phần trùng lặp. Ví dụ khi TV1 thêm thẻ connection string còn
105

---

## [Page 107] (`page-107.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
TV2 thêm thẻ globalization, bản hợp nhất phải có cả hai thẻ, không được xóa nhầm thẻ
của đồng đội. Trường hợp lỡ tay xóa sai, dùng git checkout --merge -- Web.config
để quay lại trạng thái đang xung đột rồi sửa lại từ đầu. Xung đột càng để lâu càng khó
sửa, vì vậy mỗi ngày đều merge develop mới nhất vào nhánh của mình ít nhất một lần
[2, 1].
7.5 Quản lý connection string và secret
Connection string chứa tên server, tài khoản và mật khẩu database nên tuyệt đối không
commit giá trị thật lên repo, nhất là repo public. Giải pháp gồm 2 lớp: Web.config
transform tách cấu hình theo môi trường, và secret hoặc variables của CI cung cấp giá trị
thật lúc build [10, 5, 7].
1 <?xml version = " 1.0 " encoding = " utf -8 " ? >
2 < configuration xmlns:xdt = " http: // schemas . microsoft . com / XML -
Document - Transform " >
3 < connectionStrings >
4 < add name = " AspxDb " connectionString = " Server = prod - db ; Database =
AspxDemo ; "
5 xdt:Transform = " SetAttributes " xdt:Locator = " Match ( name ) " / >
6 </ connectionStrings >
7 < system . web >
8 < compilation xdt:Transform = " RemoveAttributes ( debug ) " / >
9 < customErrors mode = " On " defaultRedirect = " ~/ Error . aspx "
10 xdt:Transform = " Replace " / >
11 </ system . web >
12 </ configuration >
Listing 43: Vi du Web Release config thay connection string khi xuat ban
File transform trên thay connection string và bật trang lỗi thân thiện khi xuất bản
bản Release, còn file Web.config gốc trong repo vẫn giữ giá trị mẫu an toàn. Giá trị
thật của server production được lưu trong GitHub Actions Secrets hoặc GitLab CI/CD
Variables, pipeline đọc secret rồi ghi đè vào file cấu hình lúc build. Secret phải bật chế độ
masked để không in ra log, và bật protected để chỉ pipeline chạy trên nhánh được bảo vệ
mới đọc được. Bảng 23 so sánh 4 nơi lưu connection string để nhóm chọn đúng chỗ cho
từng môi trường.
106

---

## [Page 108] (`page-108.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Bảng 23: So sánh 4 nơi lưu connection string và secret cho đồ án ASPX
Nơi lưu Ưu điểm Nhược điểm Dùng khi nào
Web.config giá trị thật Chạy ngay không cấu hình thêm Lộ mật khẩu cho cả nhóm và lịch sử Không bao giờ dùng
Web.config mẫu và transform An toàn, tách theo môi trường Phải viết thêm file transform Mặc định cho mọi commit
GitHub Actions Secrets Mã hóa, ẩn khỏi log Chỉ dùng trong pipeline GitHub Build và deploy từ GitHub
GitLab CI Variables Phân quyền theo môi trường Chỉ dùng trong pipeline GitLab Build và deploy từ GitLab
Nếu lỡ commit mật khẩu thật, phải đổi mật khẩu database ngay, sau đó dùng git revert
hoặc công cụ làm sạch lịch sử để xóa secret khỏi repo [2, 6, 8]. GitHub và GitLab đều
có tính năng quét secret tự động, nhóm nên bật để được cảnh báo sớm khi vô tình push
nhầm. Cuối đồ án, rà soát toàn bộ lịch sử bằng lệnh tìm kiếm chuỗi mật khẩu cũ để chắc
chắn không còn secret nào sót lại.
7.6 Mẫu lịch sử commit và quy tắc đặt message
Lịch sử commit sạch là bằng chứng nhóm làm việc nghiêm túc và giúp thầy cô theo dõi
tiến độ từng thành viên. Mọi message tuân thủ Conventional Commits: loại thay đổi,
phạm vi tùy chọn và mô tả ngắn bằng tiếng Việt không dấu hoặc tiếng Anh [3].
1 * 9 f3c1a2 ( HEAD -> develop ) docs : cap nhat checklist review Web
Forms
2 * 7 b2e44f feat : them trang DangNhap voi validation server - side
3 * 2 a91bc0 Merge pull request # 14 from feature / login - aspx
4 |\
5 | * 5 d77c91 fix : sua loi null khi Session het han
6 | * 3 e08ab4 feat : them form dang nhap Default . aspx
7 |/
8 * e6c51d0 ci : them workflow build msbuild cho NET481
9 * a4f90b3 docs : them huong dan xu ly conflict Web . config
10 * 1 c2d3e4 Merge pull request # 13 from feature / github - actions
11 * 77 aa901 chore : cap nhat gitignore chuan ASP . NET
12 * 0 b1c2d3 Initial commit : tao project Web Forms 4.8.1
Listing 44: Mau lich su commit dep cho repo do an ASPX
Khối trên cho thấy lịch sử mẫu đẹp: mỗi commit một việc, message bắt đầu bằng
feat, fix, docs, ci hoặc chore, xen kẽ các merge commit của pull request. Quy tắc
đặt message gồm 5 điểm: dùng thể mệnh lệnh như thêm và sửa thay vì đã thêm, dòng
đầu không quá 72 ký tự, tên file và hạng mục viết đúng chính tả, mỗi commit chỉ giải
quyết một việc, commit build lỗi thì sửa ngay bằng commit fix mới. Xem lịch sử bằng
git log --graph --oneline -12 để được đúng 12 dòng gọn như mẫu, dùng git show
107

---

## [Page 109] (`page-109.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
kèm mã commit để xem chi tiết từng thay đổi [2]. Trước buổi bảo vệ, TV3 xuất ảnh lịch
sử commit và ảnh pipeline xanh đưa vào báo cáo làm minh chứng nhóm đã làm đúng quy
trình.
7.7 Bài tập thực hành
Năm bài tập sau đi từ dễ đến khó, mỗi bài gắn với một kỹ năng trong chương, nhóm nên
làm theo thứ tự trong 2 tuần.
1. Dễ – Clone và commit đầu tiên: clone repo đồ án về máy, tạo nhánh feature/ho-ten,
thêm tên mình vào trang giới thiệu, commit và push lên remote. Gợi ý đáp án: đúng
3 lệnh checkout -b, commit -m theo chuẩn và push -u origin là đạt.
2. Dễ – Mở pull request và review chéo: từ nhánh ở bài 1 mở pull request về
develop, gán một bạn làm reviewer, reviewer dùng checklist 10 mục để comment
ít nhất 2 góp ý rồi approve. Gợi ý đáp án: pull request có mô tả, có ít nhất một
comment review và trạng thái đã merge.
3. Trung bình – Giải xung đột Web.config: hai bạn cùng sửa file Web.config
trên hai nhánh khác nhau rồi lần lượt merge về develop, người merge sau phải
giải xung đột và giữ được cấu hình của cả hai. Gợi ý đáp án: bản hợp nhất có đủ
connection string mẫu và thẻ mới của đồng đội, build Release thành công.
4. Khó – Thêm CI build msbuild và secret: viết workflow hoặc pipeline restore
NuGet, build project 4.8.1 bằng msbuild trên Windows runner, đọc connection
string từ Secrets hoặc Variables thay vì hard-code. Gợi ý đáp án: pipeline xanh, log
không lộ secret, pull request bị chặn merge khi build đỏ [5, 7, 9].
5. Khó – Mirror sang GitLab và bảo vệ nhánh: mirror repo GitHub sang GitLab,
mở merge request có approval rule yêu cầu một approve, so sánh 5 điểm khác nhau
giữa pull request và merge request. Gợi ý đáp án: merge request đã approve và
merge, bảng so sánh nêu được approval rule, merge train, pipeline tích hợp, quyền
hạn và self-hosted [6, 8].
Mỗi bài nộp bằng link pull request hoặc merge request kèm ảnh chụp màn hình kết
quả, không nộp file nén qua chat. TV1 chấm bài 1 và bài 3, TV2 chấm bài 2 và bài 4,
TV3 chấm bài 5 và tổng hợp điểm quá trình. Nhóm nào làm xong cả 5 bài sẽ có đủ minh
chứng cho báo cáo: lịch sử commit đẹp, pull request có review, pipeline xanh và bảng so
sánh GitHub với GitLab.
108

---

## [Page 110] (`page-110.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
8 Kết luận
Báo cáo đã đi trọn hành trình từ lệnh Git cục bộ trên máy cá nhân, qua cộng tác trực
tuyến trên GitHub và GitLab, đến quy trình làm việc nhóm gắn với đồ án ASP.NET Web
Forms trên .NET Framework 4.8.1. Chương kết luận này đối chiếu lại các mục tiêu đã
nêu ở chương mở đầu, thẳng thắn chỉ ra những việc nhóm chưa làm được, và đề xuất các
bước tiếp theo có tính khả thi cao cho học kỳ sau. Giọng văn tổng kết được ưu tiên: ngắn
gọn, chốt kết quả thay vì nhắc lại lý thuyết chi tiết.
8.1 Tổng kết: đối chiếu mục tiêu và kết quả
Nhóm đặt ra sáu mục tiêu ở chương một và đã hoàn thành cả sáu ở mức có minh chứng
chạy được, gồm lịch sử commit, Pull Request đã hợp nhất, Merge Request đã phê duyệt
và hai pipeline báo xanh [2, 6, 8]. Bảng 24 tóm tắt đối chiếu, phần liệt kê dưới đây giải
thích ngắn gọn từng mục tiêu.
1. Mục tiêu 1 – Git căn bản: nhóm đã làm chủ ba vùng làm việc, chu trình add –
commit – push, nhánh, hợp nhất và hoàn tác, minh chứng là repo demo có lịch sử
sạch và file Web.config mẫu [2]. Mỗi thành viên đều thực hiện thành thạo khoảng
hai mươi lệnh thường dùng mà không cần tra cứu.
2. Mục tiêu 2 – Git nâng cao: nhóm đã áp dụng rebase tương tác, stash, cherry-pick,
reflog, hook kiểm tra thông điệp commit và GitFlow cho repo đồ án [2, 4, 3]. Nhóm
giải thích được mô hình blob, tree và commit, cùng cách băm SHA-1 phát hiện thay
đổi một byte.
3. Mục tiêu 3 – GitHub: nhóm đã vận hành đầy đủ vòng đời fork, Pull Request,
review và hợp nhất có bảo vệ nhánh, đồng thời cấu hình GitHub Actions dùng
msbuild để biên dịch dự án 4.8.1 tới trạng thái xanh [6, 5, 9]. Pipeline lưu trữ gói
build dưới dạng artifact để đối chiếu khi phản biện.
4. Mục tiêu 4 – GitLab: nhóm đã mirror kho mã sang GitLab, vận hành Merge
Request kèm quy tắc phê duyệt và pipeline .gitlab-ci.yml trên Windows runner
cho cùng mã nguồn ASPX [8, 7]. Môi trường staging mô phỏng quy trình phát hành
nội bộ của nhóm.
5. Mục tiêu 5 – So sánh GitHub và GitLab: nhóm đã xây dựng bảng so sánh
hơn hai mươi tiêu chí về giá, CI/CD, review, bảo mật và khả năng tự lưu trữ, qua
đó trả lời được câu hỏi khi nào chọn nền tảng nào cho đồ án môn học [6, 8, 1]. Kết
luận rút ra là hai nền tảng tương đương cho bài tập nhóm, khác biệt lớn nhất nằm
ở runner và mô hình cấp phép.
109

---

## [Page 111] (`page-111.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
6. Mục tiêu 6 – Quy trình nhóm ba người: nhóm đã chốt nhánh main, develop
và feature, quy tắc Conventional Commits, checklist review Web Forms và cách
xử lý conflict file Web.config [4, 3, 10]. Mọi thay đổi đều đi qua Pull Request hoặc
Merge Request với ít nhất một lượt phê duyệt.
Mục tiêu Kết quả đạt được Minh chứng
Git căn bản Làm chủ ba vùng, nhánh và
hoàn tác
Repo demo, lịch sử log sạch
Git nâng cao Rebase, stash, hook, GitFlow Nhánh mẫu, hook chặn com￾mit sai
GitHub và Ac￾tions
PR có review, build xanh
bằng msbuild
Actions xanh, artifact build
GitLab và
pipeline
MR có approve, pipeline
Windows runner
Pipeline xanh, môi trường
staging
So sánh Bảng hơn 20 tiêu chí, khuyến
nghị chọn nền tảng
Bảng chương 6
Quy trình
nhóm
Ba nhánh, checklist review,
xử lý conflict
PR và MR đã hợp nhất
Bảng 24: Doi chieu 6 muc tieu va ket qua dat duoc
Điểm chung của cả sáu mục tiêu là mọi ví dụ đều chạy trên cùng một dự án Web
Forms 4.8.1, nên người đọc có thể kiểm chứng lại toàn bộ chỉ với ba nhóm lệnh: xem lịch
sử, xem nhánh và biên dịch thử bằng msbuild [10, 9]. Khối lệnh dưới đây tóm tắt cách
kiểm tra nhanh một máy mới sau khi nhân bản kho demo về.
1 # 1. Clone the demo repo and inspect history
2 git clone https :// github . com / nhom3 / AspxDemo_NET481 . git
3 cd AspxDemo_NET481
4 git log -- oneline -- graph -- decorate -n 12
5 git status - sb
6 git branch -a
7 # 2. Verify the protected main branch history
8 git show -- stat HEAD
9 git tag -l " v * "
10 # 3. Restore packages and build with MSBuild (. NET 4.8.1)
11 nuget restore AspxDemo . sln
12 msbuild AspxDemo . sln / p : Configuration = Release / m
Nếu cả ba nhóm lệnh trên đều chạy không lỗi và cho ra artifact Release, người chấm
có thể kết luận môi trường tái hiện của nhóm là đúng. Đây cũng là bộ kiểm tra tối thiểu
110

---

## [Page 112] (`page-112.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
mà nhóm dùng trước mỗi buổi tổng duyệt thuyết trình.
8.2 Hạn chế
Bên cạnh kết quả đạt được, nhóm xác định ba hạn chế lớn cần nêu rõ để người đọc không
hiểu lầm phạm vi của báo cáo.
• Chưa triển khai thật lên IIS: pipeline hiện dừng ở mức biên dịch và đóng gói
artifact, chưa có bước phát hành tự động lên máy chủ IIS, nên chưa kiểm chứng
được quyền thư mục, pool ứng dụng và chuỗi kết nối môi trường thật [5, 7]. Việc
phát hành vẫn làm thủ công bằng cách chép gói Release lên máy demo rồi cấu hình
tay trong IIS Manager.
• Chưa đo bao phủ kiểm thử: dự án demo mới có vài test đơn giản, chưa tích hợp
công cụ đo coverage và chưa đặt ngưỡng chặn hợp nhất khi coverage giảm, nên chưa
thể khẳng định chất lượng kiểm thử bằng số liệu [6, 8]. Nhóm mới dừng ở mức biên
dịch thành công và chạy tay các form chính.
• Chưa dựng GitLab tự lưu trữ: nhóm dùng bản SaaS trên nền tảng đám mây
thay vì tự cài máy chủ riêng, nên chưa trải nghiệm sao lưu, nâng cấp, quản lý runner
riêng và phân quyền ở quy mô quản trị viên [8]. Lý do chính là giới hạn thời gian
và máy chủ, nhóm ưu tiên làm xanh pipeline trước.
Khối lệnh dưới đây mô tả đúng quy trình thủ công hiện tại khi phát hành bản demo,
được giữ lại để thấy rõ khoảng trống mà hướng phát triển cần lấp đầy.
1 # Current manual publish ( gap to automate later )
2 msbuild AspxDemo . sln / p : Configuration = Release / p : DeployOnBuild =
true / p : PublishProfile = FolderProfile
3 # Copy output to the demo IIS folder by hand
4 xcopy / E / I / Y .\ AspxDemo \ Publish C :\ inetpub \ wwwroot \ AspxDemo
5 # No coverage gate yet : tests run without threshold
6 vstest . console . exe .\ AspxDemo . Tests \ bin \ Release \ AspxDemo . Tests .
dll
7 echo " Manual steps done . IIS config and coverage gate are still
manual . "
Nhóm coi việc ghi rõ hạn chế là một phần của phương pháp làm việc trung thực: báo
cáo chỉ khẳng định những gì đã chạy xanh, không suy diễn sang những bước chưa thực
hiện.
111

---

## [Page 113] (`page-113.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
8.3 Hướng phát triển
Từ ba hạn chế trên, nhóm đề xuất bốn hướng phát triển theo thứ tự ưu tiên, mỗi hướng
đều có đầu ra kiểm chứng được và phù hợp với năng lực sinh viên. Hình 16 minh họa lộ
trình từ trạng thái hiện tại tới tự động hóa đầy đủ.
1. Triển khai IIS tự động: bổ sung job phát hành sau job biên dịch, dùng runner có
quyền IIS để đẩy gói Release lên môi trường staging, kèm bước kiểm tra khói bằng
cách gọi trang chủ và trang đăng nhập sau khi deploy [5, 7, 9]. Tiêu chí đạt là mỗi
lần hợp nhất vào main sẽ tự tạo một bản phát hành có ghi số phiên bản.
2. Phân tích bao phủ kiểm thử: tích hợp bộ thu thập coverage cho test C# và
đặt ngưỡng tối thiểu, ví dụ hợp nhất bị chặn khi dòng mới không có test đi kèm,
báo cáo coverage được lưu thành artifact của pipeline [6, 8]. Tiêu chí đạt là biểu đồ
coverage tăng dần qua từng tuần thay vì chỉ báo đỗ hay trượt.
3. Thử mô hình monorepo cho nhiều đồ án: gom hai đến ba đồ án ASPX vào
một kho chung có cấu trúc thư mục rõ ràng, dùng đường dẫn để tách pipeline theo
từng dự án và dùng file CODEOWNERS để phân quyền review [6, 1]. Tiêu chí đạt
là sửa một form ở đồ án A không làm pipeline của đồ án B chạy lại một cách lãng
phí.
4. Tìm hiểu GitOps: dùng kho Git làm nguồn chân lý duy nhất cho cấu hình, mọi
thay đổi môi trường đều đi qua Pull Request hoặc Merge Request rồi do tác tử tự
động đồng bộ ra hạ tầng, thay vì sửa tay trên máy chủ [2, 8, 5]. Tiêu chí đạt ở mức
sinh viên là demo được vòng lặp sửa file cấu hình, hợp nhất, và quan sát môi trường
staging tự cập nhật.
Hien tai:
build xanh
Deploy IIS
tu dong
Coverage
va monorepo
GitOps
publish do luong dong bo
Hình 16: Lo trinh 4 buoc tu pipeline hien tai toi GitOps
Lộ trình trên được sắp xếp từ dễ đến khó: tự động phát hành mang lại giá trị ngay
cho môn học, đo coverage rèn kỷ luật kiểm thử, monorepo phù hợp khi nhóm có nhiều
đồ án song song, và GitOps là tầm nhìn dài hạn để nối Git với vận hành hệ thống. Nhóm
kiến nghị học kỳ sau chọn một đến hai hướng đầu tiên để triển khai trọn vẹn thay vì làm
dàn trải cả bốn hướng.
Thông điệp cuối cùng mà nhóm muốn gửi gắm là: Git giúp cá nhân làm việc chắc
chắn, GitHub và GitLab giúp nhóm cộng tác minh bạch, còn pipeline xanh giúp đồ án
ASPX 4.8.1 luôn ở trạng thái sẵn sàng demo. Khi ba lớp đó vận hành ổn định, việc học
các kỹ thuật cao hơn như review chéo, phát hành tự động và GitOps trở nên tự nhiên
112

---

## [Page 114] (`page-114.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
thay vì gượng ép. Nhóm xin cảm ơn thầy cô và các bạn đã theo dõi, mọi góp ý về quy
trình và pipeline đều được ghi nhận qua Issue để cải tiến ở phiên bản sau.
A Bảng lệnh Git tra cứu nhanh
Phụ lục này tổng hợp các lệnh Git dùng thường xuyên nhất trong học phần ASPX, sắp
xếp theo nhóm công việc từ khởi tạo kho chứa đến thao tác nâng cao. Mỗi bảng gồm bốn
cột: nhóm công việc, lệnh, mục đích và ví dụ chạy được. Sinh viên nên đọc kèm Chương
2 và Chương 3 của báo cáo để hiểu ngữ cảnh sử dụng, cùng tài liệu chính thức của Git
[2] và hướng dẫn tham khảo của Atlassian [1].
Hai ví dụ tổng hợp dưới đây minh họa luồng làm việc cơ bản và luồng làm việc theo
nhánh với project Web Forms. Mọi lệnh đều chạy được trên Git Bash hoặc PowerShell đã
cài Git.
1 # Basic workflow : config once , then add and commit
2 git config -- global user . name " Nguyen Van A "
3 git config -- global user . email " nguyenvana@example . com "
4 git init AspxDemo
5 cd AspxDemo
6 git status
7 git add .
8 git commit -m " feat : khoi tao project ASPX "
9 git log -- oneline -n 5
1 # Branch workflow : feature branch , merge , push to remote
2 git checkout -b feature /login - form
3 git add Default . aspx Default . aspx . cs
4 git commit -m " feat : them form dang nhap "
5 git checkout main
6 git merge feature /login - form
7 git remote add origin https :// github . com / lop - hk / AspxDemo . git
8 git push -u origin main
A.1 Nhóm Khởi tạo
Tạo kho chứa mới hoặc lấy kho chứa có sẵn về máy trước khi bắt đầu mọi công việc khác.
113

---

## [Page 115] (`page-115.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Nhóm Lệnh Mục đích Ví dụ
Khởi tạo git init Tạo kho Git mới trong thư
mục hiện tại
git init AspxDemo
Khởi tạo git clone <url> Sao chép toàn bộ kho chứa
từ xa về máy
git clone --depth 1 <url>
Khởi tạo git config user.nameKhai báo tên tác giả cho
commit
git config user.name "An"
Khởi tạo git config user.email Khai báo email tác giả cho
commit
git config user.email a@b.vn
Khởi tạo git config --list Liệt kê toàn bộ cấu hình
đang áp dụng
git config --global --list
Bảng 25: Bảng lệnh nhóm Khởi tạo
A.2 Nhóm Commit
Ghi lại thay đổi theo từng bước nhỏ với thông điệp rõ ràng theo Conventional Commits.
Nhóm Lệnh Mục đích Ví dụ
Commit git status Xem trạng thái Working và
Staging
git status -s
Commit git add <file> Đưa một file vào vùng
Staging
git add Default.aspx
Commit git add . Đưa mọi thay đổi vào vùng
Staging
git add -A
Commit git commit -m Chụp ảnh Staging thành
một commit
git commit -m "feat: login"
Commit git commit --amendSửa commit gần nhất thay
vì tạo mới
git commit --amend --no-edit
Bảng 26: Bảng lệnh nhóm Commit
A.3 Nhóm Lịch sử
Xem lại quá khứ của kho chứa để hiểu ai đã sửa gì và so sánh các phiên bản.
114

---

## [Page 116] (`page-116.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Nhóm Lệnh Mục đích Ví dụ
Lịch sử git log Xem lịch sử commit dạng
đầy đủ
git log -n 5
Lịch sử git log --oneline Xem lịch sử gọn một dòng
một commit
git log --oneline --graph
Lịch sử git diff So sánh Working với Stag￾ing
git diff Default.aspx
Lịch sử git diff --staged So sánh Staging với com￾mit gần nhất
git diff --cached
Lịch sử git show <commit> Xem chi tiết một commit
cụ thể
git show HEAD~1
Bảng 27: Bảng lệnh nhóm Lịch sử
A.4 Nhóm Nhánh
Mỗi tính năng làm trên một nhánh riêng để tránh đè code khi ba người cùng sửa project.
Nhóm Lệnh Mục đích Ví dụ
Nhánh git branch Liệt kê các nhánh trong
kho chứa
git branch -a
Nhánh git branch <ten> Tạo nhánh mới từ HEAD
hiện tại
git branch feature/x
Nhánh git switch <nhanh>Chuyển sang nhánh khác
an toàn
git switch main
Nhánh git switch -c <ten>Tạo và chuyển ngay sang
nhánh mới
git switch -c feature/y
Nhánh git branch -d <ten>Xóa nhánh đã merge xong git branch -d feature/x
Bảng 28: Bảng lệnh nhóm Nhánh
A.5 Nhóm Merge/Rebase
Gộp công việc từ các nhánh lại với nhau và xử lý conflict khi hai người sửa cùng một chỗ.
115

---

## [Page 117] (`page-117.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Nhóm Lệnh Mục đích Ví dụ
Merge git merge <nhanh> Gộp nhánh chỉ định vào
nhánh hiện tại
git merge feature/x
Merge git merge --abort Hủy bỏ lần merge đang dở
dang
git merge --abort
Rebase git rebase <nhanh>Đặt lại commit lên đầu
nhánh khác
git rebase main
Rebase git rebase -i HEAD~3Rebase tương tác để gộp và
sửa commit
git rebase -i HEAD~5
Rebase git cherry-pick <c>Sao chép một commit sang
nhánh hiện tại
git cherry-pick a1b2c3d
Bảng 29: Bảng lệnh nhóm Merge/Rebase
A.6 Nhóm Hoàn tác
Sửa sai an toàn: ưu tiên các lệnh tạo commit mới thay vì xóa lịch sử đã chia sẻ.
Nhóm Lệnh Mục đích Ví dụ
Hoàn tác git restore <file>Hủy sửa trong Working về
bản commit
git restore Web.config
Hoàn tác git restore --stagedGỡ file khỏi Staging giữ
nguyên sửa
git restore --staged .
Hoàn tác git reset --soft HEAD~1 Lùi một commit giữ Stag￾ing nguyên
git reset --soft HEAD~2
Hoàn tác git reset --hard HEAD Xóa mọi sửa chưa commit
về HEAD
git reset --hard origin/main
Hoàn tác git revert <commit>Tạo commit mới đảo ngược
commit cũ
git revert HEAD
Bảng 30: Bảng lệnh nhóm Hoàn tác
A.7 Nhóm Stash/Tag
Cất tạm công việc đang dở và đánh dấu các mốc phiên bản quan trọng của đồ án.
116

---

## [Page 118] (`page-118.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Nhóm Lệnh Mục đích Ví dụ
Stash git stash push -m Cất tạm sửa chưa commit
kèm ghi chú
git stash push -m "wip"
Stash git stash list Liệt kê các bản cất tạm
đang giữ
git stash list
Stash git stash pop Khôi phục bản cất tạm gần
nhất
git stash pop stash@{0}
Tag git tag <ten> Gắn thẻ phiên bản tại com￾mit hiện tại
git tag v1.0
Tag git tag -a <ten> Gắn thẻ có chú thích cho
bản phát hành
git tag -a v1.0 -m "release"
Bảng 31: Bảng lệnh nhóm Stash/Tag
A.8 Nhóm Remote
Đồng bộ kho chứa nội bộ với GitHub và GitLab để cả nhóm cùng thấy code mới nhất.
Nhóm Lệnh Mục đích Ví dụ
Remote git remote -v Liệt kê các kho chứa từ xa git remote -v
Remote git remote add origin Gắn kho chứa từ xa tên ori￾gin
git remote add upstream <url>
Remote git fetch Tải commit mới về chưa
gộp
git fetch origin
Remote git pull Tải về và gộp nhánh từ xa git pull --rebase
Remote git push Đẩy commit lên kho chứa
từ xa
git push -u origin main
Bảng 32: Bảng lệnh nhóm Remote
A.9 Nhóm Nâng cao
Các lệnh cứu hộ và dọn dẹp kho chứa khi gặp sự cố hoặc cần kiểm tra lịch sử sâu.
117

---

## [Page 119] (`page-119.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Nhóm Lệnh Mục đích Ví dụ
Nâng cao git reflog Xem lịch sử di chuyển của
HEAD
git reflog -n 10
Nâng cao git bisect start Bắt đầu tìm commit gây lỗi git bisect bad HEAD
Nâng cao git clean -fd Xóa file và thư mục chưa
theo dõi
git clean -fdn
Nâng cao git rm --cached Ngừng theo dõi file giữ lại
trên đĩa
git rm --cached app.log
Nâng cao git worktree list Liệt kê các cây làm việc
đang dùng
git worktree add ../hotfix
Bảng 33: Bảng lệnh nhóm Nâng cao
Tổng cộng phụ lục này liệt kê 45 lệnh thuộc 9 nhóm công việc, đủ cho sinh viên tra
cứu nhanh trong suốt quá trình làm đồ án ASPX theo nhóm ba người.
B Tệp gitignore mẫu cho ASP.NET
Phụ lục này cung cấp một tệp .gitignore hoàn chỉnh cho đồ án ASP.NET Web Forms
chạy trên .NET Framework 4.8.1. Mục tiêu là giữ cho kho Git gọn nhẹ: chỉ theo dõi
mã nguồn, tệp cấu hình mẫu và tài liệu, đồng thời loại bỏ mọi tệp do Visual Studio và
trình biên dịch sinh ra. Sinh viên chỉ cần sao chép nguyên văn khối mẫu ở mục dưới
đây vào tệp .gitignore đặt tại thư mục gốc của kho, sau đó thực hiện git add và
git commit như bình thường. Tệp này nằm ngay cạnh tệp giải pháp *.sln nên quy
tắc bên trong áp dụng cho toàn bộ project, bao gồm mọi thư mục con của đồ án.
Nhóm nên đưa tệp vào kho với thông điệp theo quy ước Conventional Commits, ví dụ
chore: add gitignore for Web Forms [3]. Cấu trúc phụ lục gồm ba phần: khối mẫu
đầy đủ để sao chép, phần giải thích ý nghĩa từng nhóm quy tắc, và phần hướng dẫn xử
lý khi đã lỡ commit nhầm tệp rác.
Nguyên tắc quan trọng nhất cần nhớ là: quy tắc trong .gitignore chỉ có tác dụng với
tệp chưa được Git theo dõi [2, 6]. Vì vậy, tệp .gitignore nên được tạo ngay từ commit
đầu tiên, trước khi mở project bằng Visual Studio lần đầu. Nếu tạo muộn, các thư mục
như bin/ hay packages/ có thể đã lọt vào kho, và khi đó phải xử lý thêm một bước gỡ
bỏ như hướng dẫn ở mục cuối của phụ lục này. Với đồ án Web Forms, ba nhóm cần loại
trừ nhất là kết quả biên dịch, hồ sơ cấu hình riêng của từng máy và dữ liệu cục bộ như
tệp cơ sở dữ liệu đính kèm.
118

---

## [Page 120] (`page-120.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
B.1 Nội dung mẫu
Đoạn mã dưới đây là nội dung đầy đủ của tệp .gitignore dành cho project Web Forms
trong học phần này. Mọi chú thích trong khối mã đều viết bằng tiếng Anh không dấu
để bảo đảm hiển thị đúng trên mọi trình soạn thảo và mọi hệ điều hành. Sau khi sao
chép, sinh viên chạy git status để kiểm tra: danh sách tệp mới chỉ còn mã nguồn, tệp
Web.config mẫu và tài liệu, không còn thư mục kết quả biên dịch. Quy tắc phủ ba nhóm
chính: thư mục bin/, obj/ và packages/ của quá trình build, thư mục .vs/ cùng các
tệp *.user và *.suo của Visual Studio, cuối cùng là TestResults/ và App_Data/*.mdf
chứa dữ liệu cục bộ. Thứ tự các khối trong tệp không ảnh hưởng đến kết quả, nhưng việc
nhóm theo chủ đề giúp cả nhóm dễ đọc và dễ bổ sung về sau.
1 # =============================================================
2 # . gitignore for ASP . NET Web Forms (. NET Framework 4.8.1)
3 # Place this file at the repository root and commit it first .
4 # =============================================================
5
6 # ---- 1. Build output : recreated by every build , never commit --
7 bin /
8 obj /
9 [ Dd ] ebug /
10 [ Rr ] elease /
11 x64 /
12 x86 /
13 [ Bb ]in/
14 [ Oo ] bj /
15 Generated_Code /
16
17 # ---- 2. NuGet packages : restored with " nuget restore " --------
18 packages /
19 *. nupkg
20 *. snupkg
21 project . lock . json
22 project . fragment . lock . json
23 artifacts /
24
25 # ---- 3. Visual Studio working files : per - machine state --------
26 . vs /
27 *. user
28 *. suo
29 *. userosscache
30 *. sln . docstates
119

---

## [Page 121] (`page-121.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
31 *. userprefs
32
33 # ---- 4. Test results and coverage : local run output -----------
34 TestResults /
35 *. trx
36 *. coverage
37 *. coveragexml
38 CoverageReport /
39
40 # ---- 5. Local data : attached DB and runtime files -------------
41 App_Data /*. mdf
42 App_Data /*. ldf
43 *. mdf
44 *. ldf
45
46 # ---- 6. Publish output and deployment leftovers
----------------
47 PublishProfiles /
48 *. pubxml
49 *. publish . xml
50 publish /
51 Publish /
52 app . publish /
53
54 # ---- 7. OS and editor trash : keep the repo clean --------------
55 . DS_Store
56 Thumbs . db
57 desktop . ini
58 *. tmp
59 *. temp
60 *. log
61 *. bak
62 *~
63 . idea /
64 *. swp
65 *. swo
66
67 # ---- 8. Secrets : never commit real credentials
-----------------
68 *. pfx
69 *. key
120

---

## [Page 122] (`page-122.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
70 secrets . json
71 appsettings . Development . json
Khối mẫu trên đã đủ cho hầu hết đồ án trong học phần, vì nó bao phủ toàn bộ vòng
đời làm việc với Web Forms: biên dịch, chạy thử, kiểm thử và đóng gói triển khai. Nếu
project có thêm thư mục do công cụ ngoài sinh ra, sinh viên chỉ cần thêm một dòng mới
theo đúng nhóm tương ứng rồi chạy git status để xác nhận quy tắc có hiệu lực. Một
điểm hay bị hiểu nhầm là tệp packages.config phải được giữ lại trong kho, vì đây là
danh sách thư viện giúp khôi phục đúng phiên bản trên máy khác và trên máy chủ CI
[5, 7]. Tương tự, tệp Web.config mẫu cũng phải ở lại trong kho, chỉ có các tệp cấu hình
chứa thông tin thật của từng máy mới cần loại trừ. Ngoài tệp gốc, Git còn cho phép
đặt thêm tệp .gitignore trong từng thư mục con khi cần quy tắc riêng, tuy nhiên với
đồ án này một tệp duy nhất tại thư mục gốc là đủ và dễ quản lý nhất. Khi làm việc
nhóm, mọi thay đổi với .gitignore đều nên đi qua pull request để cả nhóm cùng biết và
cùng rà soát [6, 8]. Trường hợp muốn chắc chắn một đường dẫn đã bị bỏ qua, hãy dùng
git check-ignore -v với đường dẫn đó: Git sẽ in ra dòng quy tắc đang áp dụng, như
minh họa ở mục cuối.
B.2 Giải thích từng khối
Khối kết quả biên dịch gồm bin/, obj/, Debug/ và Release/. Đây là các thư mục do
MSBuild sinh ra mỗi lần build trong Visual Studio, nên nội dung của chúng luôn có thể
tái tạo từ mã nguồn [9]. Đưa các thư mục này vào kho vừa làm kho phình to, vừa gây
xung đột không đáng có khi hai máy biên dịch ra tệp nhị phân khác nhau.
Khối gói NuGet gồm thư mục packages/ và các tệp *.nupkg. Với project .NET
Framework, các gói thư viện có thể được tải lại bằng lệnh khôi phục gói, vì vậy không cần
lưu bản sao nhị phân trong kho Git. Giữ lại tệp packages.config là đủ để mọi thành
viên phục hồi đúng phiên bản thư viện khi mở project lần đầu.
Khối tệp làm việc của Visual Studio gồm thư mục .vs/ cùng các tệp *.user và *.suo.
Đây là trạng thái riêng của từng máy như cửa sổ đang mở, điểm dừng gỡ lỗi hay đường
dẫn cục bộ, nên không có ý nghĩa chia sẻ cho cả nhóm. Mỗi sinh viên giữ các tệp này trên
máy của mình, còn kho chung chỉ lưu tệp *.sln và *.csproj dùng chung.
Khối kết quả kiểm thử gồm thư mục TestResults/ và các tệp *.trx cùng báo cáo độ
phủ. Đây là sản phẩm của mỗi lần chạy kiểm thử trên máy cá nhân, thay đổi liên tục và
không giúp ích cho việc đọc hiểu mã nguồn. Khi cần lưu bằng chứng kiểm thử cho báo
cáo, nhóm nên xuất thành tệp tài liệu riêng thay vì đẩy cả thư mục kết quả thô lên kho.
Khối dữ liệu cục bộ gồm App_Data/*.mdf, *.ldf và các tệp nhật ký cơ sở dữ liệu.
Tệp .mdf là dữ liệu SQL Server đính kèm theo project, thường nặng và chứa dữ liệu thử
nghiệm riêng của từng sinh viên. Thay vì đưa tệp nhị phân này vào kho, nhóm nên thống
nhất một đoạn lệnh tạo dữ liệu mẫu để mỗi người tự dựng cơ sở dữ liệu trên máy của
121

---

## [Page 123] (`page-123.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
mình.
Khối đầu ra đóng gói gồm Publish và các tệp *.pubxml. Đây là kết quả của bước
publish để triển khai lên máy chủ, mang tính tạm thời và phụ thuộc vào môi trường đích.
Việc loại trừ nhóm này giúp kho chỉ giữ mã nguồn và cấu hình, còn gói triển khai được
tạo mới mỗi lần phát hành.
Khối tệp rác hệ điều hành và trình soạn thảo gồm Thumbs.db, .DS_Store và các tệp
tạm. Các tệp này do Windows, macOS hoặc trình soạn thảo tự sinh ra, hoàn toàn không
liên quan đến bài làm. Cuối cùng, khối bí mật gồm *.pfx, *.key và secrets.json nhắc
cả nhóm không bao giờ đưa chứng chỉ hay khóa riêng tư vào kho, đặc biệt là kho công
khai.
Bảng dưới đây tóm tắt lại bảy nhóm quy tắc chính cùng lý do loại trừ để sinh viên
tra cứu nhanh khi cần giải thích trong buổi bảo vệ. Dòng nào trong bảng cũng tương ứng
với một khối đã liệt kê trong mẫu ở trên, nên sinh viên có thể đối chiếu trực tiếp khi cần
chỉnh sửa.
Mẫu quy tắc Nhóm tệp Lý do loại trừ
bin/, obj/ Kết quả biên dịch Tái tạo được mỗi lần build
packages/, *.nupkg Gói NuGet Khôi phục được từ mạng
.vs/, *.user, *.suo Trạng thái Visual Studio Riêng từng máy
TestResults/, *.trx Kết quả kiểm thử Thay đổi liên tục
App_Data/*.mdf Dữ liệu cục bộ Nặng, mang tính cá nhân
Publish, *.pubxml Đầu ra đóng gói Phụ thuộc môi trường đích
*.pfx, secrets.json Bí mật Rủi ro lộ thông tin
Bảng 34: Bang tom tat cac nhom quy tac gitignore cho Web Forms
B.3 Đã commit nhầm thì sửa sao
Tình huống thường gặp nhất là sinh viên quên tạo .gitignore từ đầu, mở Visual Studio
lên là build thử, sau đó mới phát hiện git status liệt kê hàng trăm tệp trong bin/ và
packages/. Trường hợp này không thể sửa chỉ bằng cách thêm .gitignore, vì Git vẫn
tiếp tục theo dõi những tệp đã lỡ đưa vào kho ở các commit trước đó [2, 1]. Cách xử lý
đúng gồm ba bước: bổ sung quy tắc bỏ qua, gỡ các tệp lỡ commit ra khỏi kho nhưng giữ
lại trên đĩa, rồi tạo một commit dọn dẹp để chốt lại. Toàn bộ thao tác đều thực hiện trên
nhánh đang làm việc, không cần tạo nhánh mới vì đây là thay đổi dọn dẹp mang tính kỹ
thuật.
Khối lệnh dưới đây thực hiện đầy đủ ba bước cho project Web Forms. Tùy chọn
--cached là điểm mấu chốt: nó chỉ xóa tệp khỏi chỉ mục của Git mà không xóa tệp thật
trên máy, nên thư mục bin/ vẫn còn nguyên để Visual Studio tiếp tục sử dụng.
122

---

## [Page 124] (`page-124.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
1 # Step 1: make sure the new rules exist , then untrack junk .
2 # -- cached keeps local files on disk , removes them from Git only .
3 git rm -- cached -r bin obj packages . vs TestResults Publish
4 git rm -- cached App_Data / site . mdf App_Data / site_log . ldf
5 git rm -- cached *. user *. suo
6
7 # Step 2: review what changed before committing .
8 git status -- short
9
10 # Step 3: record the cleanup with a clear message .
11 git add . gitignore
12 git commit -m " chore : stop tracking build output and local files "
13 git push
Sau khi đẩy commit dọn dẹp, sinh viên nên kiểm tra lại bằng khối lệnh xác minh dưới
đây. Lệnh đầu tiên hỏi Git xem một đường dẫn mẫu có đang bị bỏ qua hay không và quy
tắc nào đang áp dụng. Lệnh thứ hai liệt kê các tệp chưa được theo dõi mà Git vẫn nhìn
thấy: nếu danh sách trống hoặc chỉ còn tệp cố ý giữ lại thì việc dọn dẹp đã thành công.
Nếu lệnh kiểm tra không in ra gì, nghĩa là đường dẫn đó chưa bị bỏ qua và sinh viên cần
rà soát lại chính tả của quy tắc vừa thêm.
1 # Verify : which rule ignores a sample build artifact ?
2 git check - ignore -v bin / Debug / AspxDemo . dll
3
4 # Verify : list untracked files that Git still sees .
5 git status -- short
6 git ls - files -- others -- exclude - standard
Hình dưới đây tóm tắt quy trình ba bước từ lúc phát hiện tệp rác trong kho đến lúc
kho trở lại trạng thái sạch.
File rác đã commit Gỡ khỏi kho Kho sạch rm –cached commit
Hình 17: Quy trinh go bo file rac da commit nham
Cần phân biệt rõ hai lệnh dễ nhầm: git rm --cached chỉ gỡ tệp khỏi kho và giữ lại
tệp trên đĩa, còn git rm không có tùy chọn này sẽ xóa luôn tệp thật. Với thư mục kết quả
biên dịch thì xóa nhầm vẫn có thể build lại, nhưng với tệp dữ liệu như App_Data/*.mdf
thì xóa nhầm đồng nghĩa với mất dữ liệu thử nghiệm. Vì vậy, trước khi chạy lệnh gỡ, cả
nhóm nên sao lưu thư mục App_Data/ ra một nơi an toàn, đặc biệt khi trong đó có dữ
liệu mất nhiều thời gian chuẩn bị. Với các tệp đã từng được commit từ lâu, sau khi gỡ
khỏi kho thì lịch sử cũ vẫn còn giữ bản sao, nhưng điều này hoàn toàn bình thường và
không ảnh hưởng đến các commit mới.
123

---

## [Page 125] (`page-125.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Những cảnh báo dưới đây áp dụng cho mọi lần dọn dẹp kho, sinh viên nên đọc kỹ
trước khi thực hiện trên nhánh dùng chung.
• Không bao giờ dùng git rm thiếu tùy chọn --cached cho dữ liệu không thể tái tạo,
vì tệp trên đĩa sẽ bị xóa ngay lập tức.
• Không dùng git push --force để xóa lịch sử trên nhánh dùng chung sau khi dọn
dẹp, vì hành động này gây mất commit của thành viên khác.
• Nếu tệp lỡ commit chứa mật khẩu hoặc chuỗi kết nối thật, việc gỡ khỏi commit mới
nhất là chưa đủ: phải đổi ngay thông tin đăng nhập đó.
• Với kho công khai đã lộ bí mật, nhóm cần xem thêm hướng dẫn làm sạch lịch sử và
coi mọi thông tin từng xuất hiện trong lịch sử là đã lộ [6, 8].
• Sau khi dọn dẹp, mỗi thành viên kéo code mới về rồi biên dịch lại project để bảo
đảm mọi thứ vẫn chạy bình thường.
Sau khi hoàn tất, sinh viên mở trang kho trên GitHub hoặc GitLab để xác nhận các
thư mục bin/ và packages/ đã biến mất khỏi cây thư mục. Trang so sánh trước và sau
commit dọn dẹp cũng là minh chứng tốt để đưa vào báo cáo hoặc slide bảo vệ. Tóm lại,
tệp .gitignore chuẩn ngay từ commit đầu tiên là cách rẻ nhất để giữ kho sạch, còn lệnh
git rm --cached là lối thoát an toàn khi đã lỡ commit nhầm. Khi đã nắm vững hai công
cụ này, nhóm có thể yên tâm cộng tác trên cả GitHub và GitLab mà không còn lo kho bị
phình to vì tệp rác biên dịch [2, 6, 8]. Phụ lục này khép lại với một lời khuyên duy nhất:
tạo .gitignore trước, build project sau, và mọi rắc rối về tệp rác sẽ không bao giờ xuất
hiện. Khi kho đã sạch, nhóm quay lại quy trình làm việc thông thường với nhánh tính
năng và pull request như mô tả trong các chương chính của báo cáo.
C Mẫu CI/CD hoàn chỉnh
Phụ lục này trình bày hai mẫu tích hợp liên tục và chuyển giao liên tục hoàn chỉnh cho
dự án ASP.NET Web Forms trên .NET Framework 4.8.1. Hai mẫu này đã được rút gọn
cho khuôn khổ bài trình bày của nhóm nhưng vẫn giữ đầy đủ các bước quan trọng nhất
trong thực tế. Bạn đọc có thể sao chép trực tiếp hai tập tin bên dưới vào kho mã nguồn
của mình và điều chỉnh tên solution cho phù hợp. Toàn bộ ví dụ đều giả định solution
có tên AspxDemo_NET481.sln và dự án kiểm thử có tên AspxDemo.Tests. Các mẫu dưới
đây tuân thủ tài liệu chính thức của GitHub Actions [5, 6] và GitLab CI [7, 8]. Quy trình
build dựa trên MSBuild và bộ công cụ Visual Studio [9, 10].
Luồng chung của cả hai mẫu gồm ba giai đoạn nối tiếp nhau. Giai đoạn thứ nhất biên
dịch solution ở cấu hình Release trên máy Windows. Giai đoạn thứ hai chạy bộ kiểm thử
124

---

## [Page 126] (`page-126.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
đơn vị bằng công cụ vstest.console.exe. Giai đoạn thứ ba đóng gói thư mục publish
thành artifact để tải về hoặc triển khai tiếp. Hình 18 minh họa luồng ba giai đoạn này
một cách khái quát. Việc tách thành ba giai đoạn giúp xác định nhanh bước nào bị lỗi
khi pipeline báo đỏ.
Build Test Package bien dich kiem thu
Hình 18: Luong CI/CD ba giai doan cho du an ASPX
Khi áp dụng vào đồ án môn học, nhóm nên bắt đầu từ mẫu GitHub Actions vì chỉ
cần dùng máy chủ có sẵn của GitHub. Sau khi đã quen, nhóm có thể sao chép cùng ý
tưởng sang GitLab CI để so sánh sự khác nhau về cú pháp. Cả hai mẫu đều dùng máy
Windows vì .NET Framework 4.8.1 không biên dịch được trên máy Linux thông thường.
Lệnh dotnet build dành cho .NET hiện đại không thay thế được MSBuild trong trường
hợp này.
C.1 GitHub Actions
Mẫu trong mục này đặt tại đường dẫn .github/workflows/ci-aspx-481.yml trong
kho trên GitHub. Quy trình được kích hoạt mỗi khi có lệnh đẩy lên nhánh main hoặc
develop và mỗi khi có pull request nhắm vào hai nhánh này. Máy chạy được chọn là
windows-latest để có sẵn Visual Studio, MSBuild, NuGet và công cụ kiểm thử. Danh
sách ví dụ Lst. 45 trình bày đầy đủ nội dung tập tin workflow. Các chú thích trong khối
mã đều viết bằng tiếng Anh không dấu để giữ đúng quy tắc mã nguồn ASCII.
1 # CI for ASP.NET Web Forms 4.8.1 on GitHub Actions
2 # File : . github / workflows /ci -aspx -481. yml
3 name : ci - aspx -481
4 on :
5 push :
6 branches : [ main , develop ]
7 pull_request :
8 branches : [ main , develop ]
9 env :
10 SOLUTION : AspxDemo_NET481 . sln
11 CONFIG : Release
12 PLATFORM : "Any CPU"
13 jobs :
14 build :
15 runs - on : windows - latest
16 steps :
17 - name : Checkout code
125

---

## [Page 127] (`page-127.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
18 uses : actions / checkout@v4
19 - name : Setup MSBuild
20 uses : microsoft / setup - msbuild@v2
21 - name : Setup NuGet
22 uses : NuGet / setup - nuget@v2
23 - name : Cache NuGet packages
24 uses : actions / cache@v4
25 with :
26 path : ~/. nuget / packages
27 key : "nuget - windows -${{ hashFiles ( ’**/ packages . config ’)
}}"
28 restore - keys : nuget - windows -
29 - name : Restore packages
30 run : nuget restore $env : SOLUTION
31 - name : Build solution
32 run : msbuild $env : SOLUTION / p : Configuration = $env : CONFIG /
p : Platform ="Any CPU" / m / v : minimal / t : Rebuild
33 - name : Run unit tests
34 run : vstest . console . exe .\ Tests \ bin \ Release \ AspxDemo .
Tests . dll / Logger : trx
35 - name : Publish web project
36 run : msbuild .\ Web \ AspxDemo . csproj / p : Configuration = $env :
CONFIG / p : DeployOnBuild = true / p : WebPublishMethod =
FileSystem / p : PublishUrl = C :\ Publish \ / v : minimal
37 - name : Upload artifact
38 uses : actions / upload - artifact@v4
39 with :
40 name : aspx - package
41 path : C :\ Publish \
Listing 45: Mau GitHub Actions cho ASPX 4.8.1
Các bước trong workflow trên có thể hiểu như sau.
1. Bước Checkout code tải toàn bộ mã nguồn của lần đẩy hiện tại về máy chạy.
2. Hai bước Setup MSBuild và Setup NuGet cài đặt công cụ build chuẩn của Microsoft
vào đường dẫn hệ thống.
3. Bước Cache NuGet packages lưu thư mục gói NuGet giữa các lần chạy để giảm
thời gian tải gói. Khóa cache được tính từ nội dung các tập tin packages.config
nên cache tự động mất hiệu lực khi đổi gói.
126

---

## [Page 128] (`page-128.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
4. Bước Restore packages khôi phục các thư viện bên thứ ba trước khi biên dịch.
Nếu thiếu bước này thì MSBuild sẽ báo lỗi không tìm thấy assembly tham chiếu.
5. Bước Build solution biên dịch toàn bộ solution ở cấu hình Release với nhiều tiến
trình song song nhờ cờ /m. Cờ /t:Rebuild bảo đảm thư mục trung gian cũ bị xóa
trước khi biên dịch lại từ đầu.
6. Bước Run unit tests chạy assembly kiểm thử và xuất kết quả định dạng trx để
xem trên trang Actions. Nếu bất kỳ kiểm thử nào thất bại thì toàn bộ workflow
dừng lại và báo đỏ.
7. Hai bước cuối cùng xuất bản dự án web ra thư mục C:\Publish\ rồi tải thư mục
này lên mục artifact. Thành viên trong nhóm có thể tải artifact về để triển khai thủ
công lên Internet Information Services.
Khi mới bắt đầu, nhóm nên giữ nguyên tên nhánh main và develop như trong mẫu.
Sau này khi đã quen, nhóm có thể bổ sung thêm quy tắc bảo vệ nhánh yêu cầu workflow
phải chạy xanh mới được hợp nhất. Chuỗi kết nối cơ sở dữ liệu và các khóa bí mật tuyệt
đối không ghi trực tiếp trong tập tin YAML. Thay vào đó, nhóm khai báo secret trong
mục Settings của kho rồi tham chiếu bằng biểu thức secrets.TEN_BI_MAT. Cách làm này
giúp mã nguồn công khai nhưng thông tin nhạy cảm vẫn được bảo vệ an toàn.
C.2 GitLab CI
Mẫu trong mục này đặt tại tập tin .gitlab-ci.yml ở thư mục gốc của dự án trên GitLab.
Pipeline gồm đúng ba stage là build, test và package chạy nối tiếp nhau theo thứ tự
khai báo. Mỗi công việc đều gắn nhãn windows trong mục tags để GitLab điều phối đúng
đến máy chạy Windows. Yêu cầu này là bắt buộc vì máy chạy Linux không có MSBuild
đầy đủ cho .NET Framework 4.8.1. Danh sách ví dụ Lst. 46 trình bày đầy đủ nội dung
tập tin cấu hình.
1 # CI for ASP.NET Web Forms 4.8.1 on GitLab CI
2 # File : .gitlab -ci.yml in repository root
3 stages :
4 - build
5 - test
6 - package
7 variables :
8 SOLUTION : AspxDemo_NET481 . sln
9 CONFIG : Release
10 NUGET_PACKAGES : C :\ NuGetCache
11 cache :
12 key : nuget - $CI_COMMIT_REF_SLUG
127

---

## [Page 129] (`page-129.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
13 paths :
14 - C :\ NuGetCache \
15 before_script :
16 - echo Building $env : SOLUTION
17 build :
18 stage : build
19 tags :
20 - windows
21 script :
22 - nuget restore $env : SOLUTION
23 - msbuild $env : SOLUTION / p : Configuration = $env : CONFIG / p :
Platform ="Any CPU" / m / v : minimal / t : Rebuild
24 artifacts :
25 paths :
26 - Publish /
27 expire_in : 1 week
28 test :
29 stage : test
30 tags :
31 - windows
32 script :
33 - vstest . console . exe .\ Tests \ bin \ Release \ AspxDemo . Tests . dll /
Logger : trx
34 artifacts :
35 when : always
36 reports :
37 junit : TestResults /*. trx
38 paths :
39 - TestResults /
40 package :
41 stage : package
42 tags :
43 - windows
44 script :
45 - msbuild .\ Web \ AspxDemo . csproj / p : Configuration = $env : CONFIG
/ p : DeployOnBuild = true / p : WebPublishMethod = FileSystem / p :
PublishUrl = C :\ Publish \ / v : minimal
46 artifacts :
47 paths :
48 - C :\ Publish \
49 expire_in : 1 month
128

---

## [Page 130] (`page-130.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Listing 46: Mau GitLab CI cho ASPX 4.8.1
Ý nghĩa của từng khối trong tập tin trên được giải thích chi tiết như sau.
• Khối stages khai báo ba giai đoạn theo đúng thứ tự thực hiện trong pipeline. Nếu
một công việc ở stage trước thất bại thì các stage sau sẽ không được chạy.
• Khối variables định nghĩa các biến dùng chung như tên solution và cấu hình build.
Cách đặt biến tập trung giúp khi đổi tên solution chỉ cần sửa một chỗ duy nhất.
• Khối cache giữ lại thư mục gói NuGet giữa các lần chạy để pipeline chạy nhanh
hơn. Khóa cache dùng kèm tên nhánh nên mỗi nhánh có không gian cache riêng
biệt.
• Khối before_script in ra tên solution đang build để dễ dàng kiểm tra nhật ký khi
có nhiều dự án.
• Công việc build chạy trên máy Windows, khôi phục gói rồi biên dịch toàn bộ
solution. Thư mục Publish/ được giữ lại thành artifact trong một tuần để các
stage sau tái sử dụng.
• Công việc test chạy assembly kiểm thử và luôn xuất báo cáo kể cả khi có kiểm thử
thất bại nhờ when: always. Báo cáo định dạng trx được GitLab hiển thị trực tiếp
trong trang chi tiết của pipeline.
• Công việc package xuất bản dự án web ra thư mục C:\Publish\ và lưu lại trong một
tháng. Nhóm có thể tải gói này về để triển khai lên máy chủ Internet Information
Services của khoa.
Để pipeline trên chạy được, dự án GitLab cần có ít nhất một máy chạy Windows
đang hoạt động. Máy chạy này có thể là máy tính của thành viên trong nhóm đăng ký ở
chế độ shell hoặc máy chủ dùng chung của khoa. Khi đăng ký máy chạy, nhóm phải gắn
nhãn windows cho đúng với mục tags trong tập tin cấu hình. Nếu nhãn không khớp thì
pipeline sẽ mãi ở trạng thái chờ mà không có máy nào nhận việc. Tài liệu GitLab CI mô
tả chi tiết về stage, job, artifact và cache [7, 8].
C.3 Tham số MSBuild hay dùng
Cả hai mẫu pipeline ở trên đều gọi MSBuild với một số tham số dòng lệnh giống nhau.
Bảng 35 tổng hợp tám tham số hay dùng nhất khi biên dịch solution ASP.NET Web
Forms. Nhóm nên thuộc ý nghĩa của tám tham số này trước buổi demo vì giảng viên
thường hỏi về cờ build. Tài liệu MSBuild liệt kê đầy đủ hàng trăm tham số khác cho các
tình huống nâng cao [9].
129

---

## [Page 131] (`page-131.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Bảng 35: 8 tham so MSBuild hay dung cho ASPX
Tham số Ý nghĩa Ví dụ
/p:Configuration Chọn cấu hình biên dịch /p:Configuration=Release
/p:Platform Chọn nền tảng đích /p:Platform="Any CPU"
/m Build song song nhiều tiến trình /m
/v Mức chi tiết nhật ký /v:minimal
/t:Rebuild Xóa rồi biên dịch lại từ đầu /t:Rebuild
/t:Clean Chỉ xóa thư mục trung gian /t:Clean
/p:DeployOnBuild Xuất bản ngay khi build /p:DeployOnBuild=true
/restore Khôi phục gói NuGet trước khi build /restore
Trong tám tham số trên, ba tham số /p:Configuration, /p:Platform và /m xuất
hiện trong hầu hết mọi pipeline. Tham số /v:minimal giúp nhật ký vừa đủ chi tiết mà
không quá dài gây khó đọc trên trang web. Cặp /t:Clean và /t:Rebuild đặc biệt hữu ích
khi thư mục bin hoặc obj bị kẹt tập tin cũ. Tham số /p:DeployOnBuild=true thường đi
kèm /p:WebPublishMethod và /p:PublishUrl để xuất bản web. Tham số /restore thay
thế cho lệnh nuget restore riêng lẻ trong các dự án mới dùng PackageReference. Với dự
án ASPX cũ dùng packages.config, nhóm vẫn nên giữ bước nuget restore riêng như
trong hai mẫu trên để tránh lỗi thiếu assembly.
Tóm lại, phụ lục này cung cấp hai mẫu cấu hình sẵn sàng sao chép cho cả GitHub
Actions và GitLab CI. Nhóm chỉ cần đổi tên solution, tên dự án web và đường dẫn
assembly kiểm thử là có pipeline chạy xanh. Khi đã có pipeline xanh, nhóm nên bổ sung
thêm kiểm tra chất lượng mã và quét bảo mật ở các bước tiếp theo. Việc nắm vững tám
tham số MSBuild trong Bảng 35 giúp nhóm tự tin giải thích trước giảng viên. Nhóm nên
lưu hai mẫu này vào kho tài liệu chung để tái sử dụng cho các đồ án tiếp theo.
D Kịch bản demo trên lớp
Phụ lục này trình bày kịch bản demo trực tiếp trên lớp của nhóm 3 thành viên cho đề tài
Git, GitHub và GitLab gắn với project ASP.NET Web Forms chạy trên .NET Framework
4.8.1. Tổng thời gian demo từ 15 đến 18 phút, mỗi thành viên đảm nhận một phần từ
5 đến 7 phút theo đúng phân công đã thống nhất từ đầu học phần. Mọi bước demo
đều được diễn tập trước, có lệnh chạy được, có kết quả mong đợi rõ ràng và có phương
án dự phòng khi gặp sự cố mạng hoặc máy chiếu. Nhóm sử dụng một project mẫu tên
AspxDemo_NET481 gồm một trang Default.aspx, một file cấu hình Web.config và một
thư viện lớp viết bằng ngôn ngữ C# [2, 10]. Trước giờ demo, nhóm kiểm tra repo GitHub
và project GitLab đều ở trạng thái sạch, pipeline gần nhất báo xanh và không còn pull
request hay merge request nào đang mở dở. Người giữ giờ là TV3, có nhiệm vụ ra hiệu
130

---

## [Page 132] (`page-132.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
khi mỗi phần còn một phút và quyết định cắt gọn bước nào nếu thời gian bị lố.
Ba phần demo liên kết thành một câu chuyện duy nhất: TV1 tạo lịch sử Git local,
TV2 đưa code lên GitHub và review qua pull request, TV3 mirror sang GitLab và phát
hành qua pipeline. Hình 19 tóm tắt luồng demo này để khán giả dễ theo dõi ngay từ đầu
buổi trình bày.
TV1 Git local TV2 GitHub TV3 GitLab
push mirror
Hình 19: Luồng demo tổng thể từ Git local lên GitHub và GitLab
D.1 Demo TV1: Git local
TV1 demo Git hoàn toàn offline trên máy tính cá nhân để chứng minh Git là hệ thống
phân tán, không cần mạng vẫn commit, branch và merge được [2, 1]. Mục tiêu sau 6 phút:
khán giả hiểu vùng làm việc, vùng staging và kho chứa, đồng thời thấy cách giải quyết
conflict trên file Web.config. TV1 mở sẵn hai cửa sổ: một cửa sổ dòng lệnh và một cửa
sổ Visual Studio 2022 mở project AspxDemo_NET481. Toàn bộ lệnh trong phần này được
gom lại trong Danh mục 47 để khán giả chụp ảnh và thực hành lại sau buổi học.
1 # 0. check tools ( run once before class )
2 git -- version
3 git config -- global user . name " TV1 Demo "
4 git config -- global user . email " tv1@demo . local "
5 # 1. init repo and first commit
6 mkdir AspxDemo_NET481 && cd AspxDemo_NET481
7 git init -b main
8 # create minimal Web Forms files for demo
9 printf ’ <% @ Page Language =" C #" % >\n < html > < body > < h1 > Demo </ h1 > </
body > </ html >\ n ’ > Default . aspx
10 printf ’ <? xml version ="1.0"? >\ n < configuration >\ n </ configuration >\
n ’ > Web . config
11 printf ’ bin /\ nobj /\ npackages /\ n . vs /\ n ’ > . gitignore
12 git add -A
13 git commit -m " feat : khoi tao project ASPX 4.8.1 "
14 # 2. branch , conflict , stash , tag ( see steps below )
15 git branch feature /login - aspx
16 git log -- oneline -- graph -n 5
17 git status - sb
Listing 47: Tập lệnh Git local của TV1
Mười lăm bước chi tiết của TV1 như sau:
131

---

## [Page 133] (`page-133.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
1. Kiểm tra phiên bản Git bằng git --version và cấu hình danh tính bằng git config --global user.name
và git config --global user.email. Nói rõ mỗi commit luôn gắn tên và email
người tạo để truy vết trách nhiệm trong nhóm.
2. Khởi tạo kho chứa mới bằng git init -b main ngay trong thư mục AspxDemo_NET481
đã chuẩn bị sẵn. Giải thích thư mục ẩn .git là toàn bộ lịch sử, xóa thư mục này
coi như xóa lịch sử Git.
3. Tạo khung project ASPX tối thiểu gồm Default.aspx, Web.config và file .gitignore
chuẩn cho ASP.NET để loại thư mục bin, obj, packages và .vs. Mở file .gitignore
trên máy chiếu và giải thích vì sao không commit các thư mục build.
4. Thêm toàn bộ file vào vùng staging bằng git add -A, kiểm tra bằng git status -sb
rồi tạo commit đầu tiên theo Conventional Commits [3]. Commit mẫu: feat: khoi tao project ASPX 4.8.1
để khán giả thấy message viết thường, có tiền tố rõ ràng.
5. Xem lịch sử bằng git log --oneline --graph và git show HEAD --stat để chứng
minh commit vừa tạo đã nằm trong kho chứa. Nhấn mạnh Git đã lưu snapshot toàn
bộ project mà chưa cần bất kỳ server nào.
6. Tạo nhánh tính năng bằng git branch feature/login-aspx rồi chuyển sang nhánh
này bằng git switch feature/login-aspx. Giải thích nhánh trong Git chỉ là con
trỏ nhẹ trỏ tới commit, tạo nhánh gần như tức thì [2, 4].
7. Trên nhánh tính năng, sửa file Default.aspx thêm dòng chào mừng, sau đó commit
bằng git commit -am "feat: them dong chao tren trang chu". Chạy git log --oneline -n 3
để khán giả thấy nhánh tính năng đã đi trước nhánh chính một commit.
8. Quay về nhánh chính bằng git switch main, sửa cùng vùng trong file Web.config
như đã hẹn trước, ví dụ thêm một khóa cấu hình có tên AppTitle. Commit thay
đổi này trên nhánh chính để cố ý tạo tình huống hai nhánh sửa cùng một chỗ.
9. Thực hiện git merge feature/login-aspx và để Git báo conflict trên file Web.config
ngay trước mặt khán giả. Mở file conflict, chỉ rõ ba phần: vùng của nhánh chính,
dấu phân cách và vùng của nhánh tính năng.
10. Giải quyết conflict bằng cách giữ cả hai ý: giữ khóa AppTitle của nhánh chính và giữ
nội dung chào của nhánh tính năng ở file giao diện. Chạy git add Web.config rồi
git commit để hoàn tất commit merge, sau đó chiếu đồ thị bằng git log --oneline --graph -n 6.
11. Demo lệnh git stash cho tình huống đang sửa dở file mà phải chuyển nhánh
gấp: sửa file, chạy git stash push -m "wip", chuyển nhánh, rồi quay lại chạy
git stash pop. Giải thích stash là ngăn xếp tạm, phù hợp cho việc cất nhanh thay
đổi chưa đủ tốt để commit.
132

---

## [Page 134] (`page-134.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
12. Demo gắn thẻ phiên bản bằng git tag -a v1.0 -m "ban demo tren lop" rồi liệt
kê bằng git tag --list và xem chi tiết bằng git show v1.0. Nói rõ tag dùng để
đánh dấu bản phát hành, khác với nhánh vì tag không di chuyển theo commit mới.
13. Liệt kê nhánh bằng git branch -a và xóa nhánh tính năng đã merge xong bằng
git branch -d feature/login-aspx. Giải thích chỉ xóa nhánh đã merge xong,
giữ nhánh chính sạch và tránh nhầm lẫn khi bàn giao repo cho TV2.
14. Minh họa hoàn tác an toàn bằng git revert HEAD --no-edit trên một commit
thử, rồi xem lịch sử để thấy lịch sử chỉ thêm chứ không mất. Nhấn mạnh nhóm luôn
ưu tiên revert thay vì reset trên nhánh đã push để không viết lại lịch sử chung.
15. Chốt phần demo bằng git status -sb, git branch -vv và git log --oneline --graph -n 8
để khán giả thấy trạng thái sạch và lịch sử đẹp trước khi bàn giao cho TV2. Nhắc
lại ba vùng Git và khẳng định toàn bộ phần này chạy offline, không cần GitHub
hay GitLab.
Tiêu chí đạt của TV1: có ít nhất 4 commit, 1 commit merge giải quyết conflict
Web.config, 1 stash đã pop xong và 1 tag tên v1.0. Nếu còn dư một phút, TV1 mở
thêm lệnh git diff HEAD~1 HEAD --stat để minh họa cách review thay đổi trước khi
push.
D.2 Demo TV2: GitHub
TV2 tiếp nối repo local của TV1, đưa code lên GitHub rồi thực hiện quy trình pull request
chuẩn có review và kiểm tra CI [6, 5]. Mục tiêu sau 6 phút: khán giả hiểu vì sao nhóm
cấm push thẳng nhánh chính và cách GitHub Actions build project .NET Framework
4.8.1 bằng msbuild. TV2 mở sẵn trình duyệt ở trang repo GitHub, file ci-aspx-481.yml
và thẻ Actions để chuyển cảnh nhanh, tránh gõ địa chỉ trên lớp. Toàn bộ lệnh đẩy code
và tạo pull request bằng dòng lệnh được gom trong Danh mục 48.
1 # 0. link local repo to GitHub ( done once before class )
2 git remote add origin https :// github . com / nhom3 / aspx - demo . git
3 git remote -v
4 # 1. push main and feature branch
5 git push -u origin main
6 git push -u origin feature /login - aspx
7 # 2. create pull request from CLI ( optional , can use web UI )
8 gh pr create -- base main -- head feature /login - aspx \
9 -- title " feat : trang dang nhap ASPX " \
10 -- body " Mo ta ngan , anh chup man hinh , cach kiem thu . "
11 # 3. check status and merge after green CI
12 gh pr checks -- watch
133

---

## [Page 135] (`page-135.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
13 gh pr merge -- squash -- delete - branch
14 git switch main
15 git pull --ff - only
Listing 48: Đẩy code và tạo pull request trên GitHub
Tám bước chi tiết của TV2 như sau:
1. Liên kết repo local với GitHub bằng git remote add origin trỏ tới địa chỉ repo
của nhóm, kiểm tra bằng git remote -v. Đẩy nhánh chính bằng git push -u origin main
và giải thích cờ -u giúp lần sau chỉ cần gõ git push.
2. Đẩy nhánh tính năng bằng git push -u origin feature/login-aspx, sau đó mở
trang repo trên trình duyệt để khán giả thấy nhánh mới vừa xuất hiện. Nhấn mạnh
code đã rời máy cá nhân và nằm an toàn trên server GitHub.
3. Mở pull request từ nhánh tính năng về nhánh chính bằng nút trên web hoặc bằng
lệnh gh pr create như trong Danh mục 48. Tiêu đề pull request tuân thủ Conven￾tional Commits, mô tả ghi rõ thay đổi gì, kiểm thử thế nào và đính kèm ảnh chụp
màn hình trang Default.aspx.
4. Nhờ TV1 đóng vai reviewer ngay trên lớp: reviewer mở thẻ Files changed, bình luận
vào đúng dòng thêm khóa AppTitle trong file Web.config. TV2 sửa theo góp ý,
commit thêm một lần rồi đẩy tiếp lên cùng nhánh để khán giả thấy pull request tự
cập nhật.
5. Chờ GitHub Actions chạy pipeline build msbuild cho .NET Framework 4.8.1, chiếu
thẻ Checks đang chuyển từ màu vàng sang màu xanh [5, 9]. Giải thích pipeline gồm
các bước: lấy code, phục hồi gói NuGet, build solution ở chế độ Release và chạy test
đơn giản.
6. Demo nhánh chính được bảo vệ: thử push thẳng vào main và để GitHub từ chối,
qua đó chứng minh quy tắc nhóm là mọi thay đổi phải qua pull request. Chỉ rõ ba
lớp bảo vệ: yêu cầu pull request, yêu cầu ít nhất một approve và yêu cầu kiểm tra
CI phải xanh.
7. Khi CI báo xanh và đã có một approve, TV2 bấm Squash and merge, xóa nhánh
tính năng từ xa, rồi về máy local chạy git switch main và git pull --ff-only.
Chiếu đồ thị log sau khi merge để khán giả thấy lịch sử nhánh chính gọn gàng chỉ
còn một commit tính năng.
8. Chốt phần demo bằng cách mở thẻ Insights rồi mở tiếp trang Actions vừa chạy
xanh để khẳng định code ASPX 4.8.1 đã được build tự động thành công. Bàn giao
cho TV3 bằng câu chốt: code đã sẵn sàng để mirror sang GitLab và đi tiếp pipeline
phát hành.
134

---

## [Page 136] (`page-136.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Tiêu chí đạt của TV2: có một pull request đã merge sau review, một lần push thẳng bị
chặn để minh họa protected branch và một pipeline Actions báo xanh. Nếu mạng chậm,
TV2 dùng sẵn ảnh chụp pipeline xanh trong slide dự phòng và tiếp tục thuyết minh mà
không dừng buổi demo.
D.3 Demo TV3: GitLab
TV3 mirror repo từ GitHub sang GitLab rồi thực hiện quy trình merge request có phê
duyệt và pipeline nhiều giai đoạn [8, 7]. Mục tiêu sau 6 phút: khán giả phân biệt được
pull request và merge request, hiểu approval rules và thấy environments của GitLab trỏ
tới bản staging và bản production. TV3 mở sẵn ba thẻ trình duyệt: trang project GitLab,
thẻ Merge requests và thẻ CI/CD Pipelines để chuyển cảnh mượt mà. Đoạn cấu hình CI
mẫu dùng trong demo được rút gọn trong Danh mục 49 với chú thích hoàn toàn bằng
tiếng Anh không dấu.
1 # Minimal GitLab CI for ASPX 4.8.1 on Windows runner
2 stages : [ build , test , deploy ]
3 variables :
4 NUGET_PATH : ’C:\ NuGet \ nuget .exe ’
5 MSBUILD_PATH : ’C:\ MSBuild \ msbuild .exe ’
6 build_web :
7 stage : build
8 tags : [ windows , msbuild ]
9 script :
10 - ’% NUGET_PATH % restore AspxDemo .sln ’
11 - ’% MSBUILD_PATH % AspxDemo .sln /p: Configuration = Release ’
12 artifacts :
13 paths : [’Publish /’]
14 expire_in : 1 week
15 test_web :
16 stage : test
17 tags : [ windows , msbuild ]
18 script :
19 - ’VSTest . Console .exe Tests .dll ’
20 needs : [ build_web ]
21 deploy_staging :
22 stage : deploy
23 tags : [ windows , msbuild ]
24 script :
25 - ’echo Deploy to staging folder ’
26 environment :
27 name : staging
135

---

## [Page 137] (`page-137.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
28 url : https :// staging . demo . local
29 when : manual
Listing 49: Pipeline GitLab CI rút gọn cho ASPX 4.8.1
Tám bước chi tiết của TV3 như sau:
1. Tạo project GitLab bằng chức năng mirror từ URL repo GitHub, đặt chế độ public
trong buổi học để khán giả tiện theo dõi [8]. Chiếu màn hình cấu hình mirror và
nhấn nút cập nhật ngay để khán giả thấy commit từ GitHub chảy sang GitLab sau
vài giây.
2. Tạo nhánh feature/gitlab-ci trên GitLab, thêm file .gitlab-ci.yml theo nội
dung Danh mục 49 rồi đẩy nhánh lên bằng lệnh push thông thường. Giải thích ba
stages build, test và deploy cùng ý nghĩa của artifacts lưu gói publish sau khi
build.
3. Mở merge request từ nhánh feature/gitlab-ci về nhánh chính, gán TV2 làm
approver và gán nhãn ci để dễ lọc. Chỉ rõ điểm khác tên gọi: GitHub dùng pull
request còn GitLab dùng merge request nhưng bản chất đều là đề xuất hợp nhất có
review.
4. Demo approval rules: merge request yêu cầu ít nhất một approve, đang ở trạng thái
chưa đủ điều kiện merge nên nút Merge bị mờ. Nhờ TV2 bấm Approve ngay trên
lớp, nút Merge sáng lên để khán giả thấy rõ vai trò của phê duyệt bắt buộc.
5. Chờ pipeline chạy trên Windows runner có gắn thẻ windows và msbuild, chiếu
từng job chuyển từ chờ sang chạy rồi sang xanh [7, 9]. Giải thích vì sao project
.NET Framework 4.8.1 cần runner Windows thay vì runner Linux thông thường:
chỉ Windows mới có đầy đủ msbuild và thư viện Web Forms.
6. Khi pipeline báo xanh, TV3 bấm Merge để hợp nhất, sau đó mở lại thẻ Pipelines
để chỉ pipeline đã hoàn tất sau merge. Chiếu đồ thị log sau merge để khẳng định
nhánh chính đã nhận code từ nhánh tính năng một cách an toàn.
7. Mở thẻ Environments để chỉ hai môi trường staging và production đã khai báo
sẵn trong file YAML. Bấm nút deploy thủ công cho môi trường staging để minh
họa bước phát hành có kiểm soát thay vì tự động đẩy thẳng production.
8. Mở trang so sánh nhanh GitHub và GitLab trong một bảng một slide: điểm mạnh
của GitHub là cộng đồng và Actions, điểm mạnh của GitLab là pipeline tích hợp và
self-hosted. Kết luận phần demo bằng thông điệp: nhóm dùng GitHub cho bài tập
mở, dùng GitLab khi cần kiểm soát pipeline và môi trường chặt chẽ hơn.
136

---

## [Page 138] (`page-138.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
Tiêu chí đạt của TV3: có mirror đồng bộ thành công, một merge request đã được
approve và merge, một pipeline xanh và một environment staging có bản deploy mẫu.
Nếu pipeline xếp hàng lâu, TV3 chuyển ngay sang ảnh chụp pipeline xanh đã chuẩn bị
và tiếp tục giảng phần so sánh để không làm mất nhịp buổi demo.
D.4 Dự phòng sự cố
Kịch bản dự phòng giúp buổi demo không bị gián đoạn dù gặp sự cố mạng, máy chiếu
hay lỗi thao tác của người trình bày. Nguyên tắc chung: mọi nội dung quan trọng đều có
ảnh chụp dự phòng, mọi lệnh dài đều có file script chạy sẵn và luôn có một thành viên
sẵn sàng nói thay 30 giây. Bảng 36 liệt kê 5 tình huống hay gặp nhất cùng dấu hiệu nhận
biết và cách xử lý trong vòng một phút.
Bảng 36: Các sự cố thường gặp khi demo và cách xử lý nhanh
Tình huống Dấu hiệu Cách xử lý trong một phút
Mất mạng Không push được,
trang GitHub quay
vòng
Chuyển sang demo offline của
TV1, dùng ảnh pipeline xanh có
sẵn và tiếp tục thuyết minh
CI xếp hàng
lâu
Job treo ở trạng thái
chờ quá 2 phút
Mở ảnh pipeline xanh dự phòng,
giải thích file YAML trong lúc
chờ, không đứng im nhìn màn
hình
Merge bị con￾flict nặng
Thông báo conflict
nhiều file, khó sửa
nhanh
Hủy merge bằng lệnh hủy, quay
về bản sạch đã chuẩn bị, hẹn
khán giả xem lại sau giờ học
Quên lời
thuyết minh
Người nói ngập ngừng,
bỏ sót bước
Người giữ giờ nhắc ý chính qua
giấy cue-card, người còn lại nói
thay 30 giây đúng phần việc của
mình
Máy chiếu mờ
chữ
Khán giả kêu không
đọc được lệnh
Tăng cỡ chữ terminal lên 18pt,
chỉ chiếu từng lệnh ngắn, đọc to
lệnh trước khi Enter
Ngoài bảng trên, nhóm chuẩn bị thêm một USB chứa toàn bộ repo, slide PDF và báo
cáo PDF để demo offline hoàn toàn khi phòng học mất Internet. Mỗi thành viên thuộc
lòng lệnh hủy an toàn: hủy merge chưa commit, quay về commit sạch gần nhất và kiểm
tra trạng thái sạch trước khi làm tiếp. TV3 giữ một tờ cue-card ghi thứ tự micro, mật
khẩu máy chiếu và đường dẫn tới ảnh dự phòng để không phải tìm kiếm lúng túng trên
lớp. Buổi tổng duyệt yêu cầu mỗi người chạy toàn bộ phần demo của mình hai lần liền
137

---

## [Page 139] (`page-139.png`)

GIT – GitHub – GitLab Hoc phan ASPX – .NET 4.8.1
mạch, lần hai phải nhanh hơn lần một ít nhất một phút. Thông điệp chốt gửi tới lớp: Git
giúp làm việc nhóm an toàn, GitHub và GitLab giúp review và kiểm tra tự động, kỷ luật
nhánh và pipeline xanh là thước đo chất lượng nhóm.
Tài liệu
[1] Atlassian. Learn git: Tutorials, branching, merging va workflows. https://www.
atlassian.com/git, 2026. Truy cap thang 11 nam 2026.
[2] Scott Chacon and Ben Straub. Pro Git. Apress, https://progit.org, second edition,
2014. Sach mo, doc truc tuyen mien phi tai progit.org.
[3] Conventional Commits. Conventional commits 1.0.0 specification. https://www.
conventionalcommits.org/, 2026. Truy cap thang 11 nam 2026.
[4] Vincent Driessen. A successful git branching model. https://nvie.com/posts/
a-successful-git-branching-model/, 2010. Truy cap thang 11 nam 2026.
[5] GitHub. Github actions documentation: Workflows, events va windows runners.
https://docs.github.com/en/actions, 2026. Truy cap thang 11 nam 2026.
[6] GitHub. Github docs: Hello world, pull requests, issues va code review. https:
//docs.github.com/, 2026. Truy cap thang 11 nam 2026.
[7] GitLab. Gitlab ci/cd documentation: Pipelines, jobs, artifacts va runners. https:
//docs.gitlab.com/ee/ci/, 2026. Truy cap thang 11 nam 2026.
[8] GitLab. Gitlab documentation: Projects, groups, issues va merge requests. https:
//docs.gitlab.com/, 2026. Truy cap thang 11 nam 2026.
[9] Microsoft. Msbuild reference for .net framework projects. https://learn.
microsoft.com/en-us/visualstudio/msbuild/msbuild, 2026. Truy cap thang 11
nam 2026.
[10] Microsoft. .net framework 4.8.1 developer guide. https://learn.microsoft.com/
en-us/dotnet/framework/, 2026. Truy cap thang 11 nam 2026.
138

---


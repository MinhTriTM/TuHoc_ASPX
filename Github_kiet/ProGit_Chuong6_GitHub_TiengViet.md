# SÁCH PRO GIT (TÁC GIẢ: SCOTT CHACON & BEN STRAUB)
## BẢN DỊCH TIẾNG VIỆT — CHƯƠNG 6: GITHUB (ĐẦY ĐỦ VÀ CHUẨN KỸ THUẬT)

> **Nguyên tác:** *Pro Git (Second Edition)*, Chapter 6: GitHub (trang 172–223)  
> **Tác giả:** Scott Chacon & Ben Straub  
> **Người dịch & Hiệu đính:** Thành viên 2 (TV2 — Kiệt)  
> **Không gian lưu trữ:** [Github_kiet](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/Github_kiet)  
> **Tài liệu đối chiếu:** [progit.pdf](file:///T:/HK1_26_27/Lap_trinh_aspx/TuHoc_ASPX/Github_kiet/progit.pdf)  

---

### MỤC LỤC CHƯƠNG 6

1. [Lời Giới Thiệu Chương 6](#1-lời-giới-thiệu-chương-6)
2. [6.1 Thiết lập và Cấu hình Tài khoản (Account Setup and Configuration)](#61-thiết-lập-và-cấu-hình-tài-khoản)
   - [Đăng ký tài khoản](#đăng-ký-tài-khoản)
   - [Truy cập qua SSH (SSH Access)](#truy-cập-qua-ssh)
   - [Mã truy cập cá nhân (Personal Access Tokens - PAT)](#mã-truy-cập-cá-nhân)
   - [Ảnh đại diện (Avatar)](#ảnh-đại-diện)
   - [Địa chỉ Email (Email Addresses)](#địa-chỉ-email)
   - [Xác thực hai yếu tố (Two Factor Authentication - 2FA)](#xác-thực-hai-yếu-tố)
3. [6.2 Đóng góp vào một Dự án (Contributing to a Project)](#62-đóng-góp-vào-một-dự-án)
   - [Tạo bản sao Fork (Creating a Fork)](#tạo-bản-sao-fork)
   - [Quy trình GitHub Flow (The GitHub Flow)](#quy-trình-github-flow)
   - [Tạo Yêu cầu Kéo mã nguồn (Creating a Pull Request)](#tạo-yêu-cầu-kéo-mã-nguồn)
   - [Thảo luận và Tinh chỉnh trên Pull Request (Iterating on a Pull Request)](#thảo-luận-và-tinh-chỉnh-trên-pull-request)
   - [Xử lý xung đột khi Pull Request không thể trộn sạch](#xử-lý-xung-đột-khi-pull-request-không-thể-trộn-sạch)
   - [Cú pháp Markdown đặc thù của GitHub (GitHub Flavored Markdown - GFM)](#cú-pháp-markdown-đặc-thù-của-github)
   - [Giữ cho kho lưu trữ của bạn luôn cập nhật (Keep your GitHub repo up to date)](#giữ-cho-kho-lưu-trữ-của-bạn-luôn-cập-nhật)
4. [6.3 Quản trị và Duy trì Dự án (Maintaining a Project)](#63-quản-trị-và-duy-trì-dự-án)
   - [Tạo một kho lưu trữ mới (Creating a New Repository)](#tạo-một-kho-lưu-trữ-mới)
   - [Thêm cộng tác viên (Adding Collaborators)](#thêm-cộng-tác-viên)
   - [Quản lý các Yêu cầu Kéo mã (Managing Pull Requests)](#quản-lý-các-yêu-cầu-kéo-mã)
   - [Các tham chiếu Pull Request đặc biệt (Pull Request Refs)](#các-tham-chiếu-pull-request-đặc-biệt)
   - [Kéo mã vào các nhánh tính năng](#kéo-mã-vào-các-nhánh-tính-năng)
   - [Đề cập và Hệ thống Thông báo (Mentions and Notifications)](#đề-cập-và-hệ-thống-thông-báo)
   - [Các tệp tin quy ước đặc biệt (Special Files: README, CONTRIBUTING, LICENSE)](#các-tệp-tin quy-ước-đặc-biệt)
   - [Quản trị dự án (Project Administration)](#quản-trị-dự-án)
5. [6.4 Quản lý Tổ chức (Managing an Organization)](#64-quản-lý-tổ-chức)
   - [Cơ bản về Tổ chức (Organization Basics)](#cơ-bản-về-tổ-chức)
   - [Nhóm làm việc (Teams)](#nhóm-làm-việc)
   - [Nhật ký kiểm toán (Audit Log)](#nhật-ký-kiểm-toán)
6. [6.5 Viết Kịch bản Tự động hóa với GitHub (Scripting GitHub)](#65-viết-kịch-bản-tự-động-hóa-với-github)
   - [Dịch vụ và Webhooks (Services and Webhooks)](#dịch-vụ-và-webhooks)
   - [Giao diện lập trình ứng dụng GitHub API (The GitHub API)](#giao-diện-lập-trình-ứng-dụng-github-api)
7. [6.6 Tổng Kết Chương (Summary)](#66-tổng-kết-chương)
8. [Phụ Lục Kỹ Thuật: Cập Nhật Hiện Đại Hóa & Ứng Dụng Trong Học Phần ASPX](#phụ-lục-kỹ-thuật)

---

## 1. LỜI GIỚI THIỆU CHƯƠNG 6

GitHub là máy chủ lưu trữ các kho Git lớn nhất hiện nay trên thế giới, đóng vai trò là tâm điểm cộng tác của hàng triệu lập trình viên và dự án phần mềm. Một tỷ lệ rất lớn các kho chứa Git được lưu trữ trên GitHub, và vô số dự án nguồn mở sử dụng nó cho việc hosting mã nguồn, theo dõi vấn đề (issue tracking), đánh giá mã nguồn (code review) cùng nhiều tính năng khác.

Do đó, mặc dù GitHub không phải là một phần trực tiếp của dự án mã nguồn mở Git (Git là phần mềm công cụ độc lập do Linus Torvalds khởi xướng), nhưng có khả năng rất cao là bạn sẽ cần hoặc muốn tương tác với GitHub tại một thời điểm nào đó trong sự nghiệp làm việc chuyên nghiệp với Git.

Chương này tập trung vào việc **sử dụng GitHub một cách hiệu quả**. Chúng ta sẽ cùng nhau tìm hiểu:
- Đăng ký và quản trị tài khoản cá nhân;
- Khởi tạo và sử dụng các kho lưu trữ Git;
- Các quy trình làm việc phổ biến (workflows) để đóng góp mã nguồn cho dự án người khác cũng như tiếp nhận đóng góp từ cộng đồng vào dự án của chính bạn;
- Giao diện lập trình của GitHub (API) cùng nhiều mẹo thực tế hữu ích giúp quy trình phát triển phần mềm của bạn trở nên thuận tiện hơn.

> [!NOTE]
> **Giao diện người dùng có thể thay đổi theo thời gian:**  
> Vì GitHub là một dịch vụ web thương mại liên tục cải tiến, giao diện trang web có thể thay đổi đôi chút so với các ảnh chụp màn hình trong sách. Tuy nhiên, các nguyên lý và kiến trúc làm việc cốt lõi của Git trên GitHub luôn duy trì tính nhất quán bền vững.

---

## 6.1 THIẾT LẬP VÀ CẤU HÌNH TÀI KHOẢN (ACCOUNT SETUP AND CONFIGURATION)

Điều đầu tiên bạn cần làm là thiết lập một tài khoản người dùng cá nhân miễn phí. Hãy truy cập `https://github.com`, chọn tên người dùng (username) chưa bị ai đăng ký, cung cấp địa chỉ email và mật khẩu của bạn, sau đó nhấp vào nút **Sign up for GitHub**.

### Đăng ký tài khoản
Ngay sau khi đăng ký, GitHub sẽ hiển thị trang biểu phí nâng cấp (bạn có thể bỏ qua phần này vì tài khoản miễn phí đã hỗ trợ đầy đủ các tính năng cơ bản). Tiếp theo, GitHub sẽ gửi một email xác thực đến hòm thư bạn vừa đăng ký. Hãy mở email và xác minh ngay lập tức — bước này rất quan trọng để kích hoạt đầy đủ quyền tạo kho và mở Pull Request.

> [!TIP]
> Tài khoản GitHub miễn phí cung cấp gần như toàn bộ tính năng cốt lõi cho việc lưu trữ mã nguồn mở lẫn kho chứa riêng tư (Private Repositories). Các gói trả phí hướng tới doanh nghiệp hoặc tổ chức cần các giới hạn nâng cao về băng thông lưu trữ và dung lượng máy ảo CI/CD.

### Truy cập qua SSH (SSH Access)
Mặc dù bạn hoàn toàn có thể sử dụng kết nối HTTP với tên người dùng và mật khẩu (hoặc Personal Access Token), nhưng việc thiết lập khóa công khai SSH (SSH Public Key) là giải pháp tiện lợi và an toàn nhất khi làm việc từ dòng lệnh.

1. **Kiểm tra và tạo khóa SSH trên máy cá nhân:**  
   Nếu bạn chưa có cặp khóa SSH, hãy mở terminal và chạy lệnh:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "email_cua_ban@example.com"
   ```
   *(Ghi chú hiện đại: Hiện nay GitHub khuyến khích sử dụng thuật toán Ed25519: `ssh-keygen -t ed25519 -C "email@example.com"`)*.

2. **Thêm khóa công khai lên GitHub:**
   - Mở phần cài đặt tài khoản bằng cách nhấp vào biểu tượng ảnh đại diện ở góc trên cùng bên phải màn hình -> chọn **Settings**.
   - Chọn mục **SSH and GPG keys** ở thanh trình đơn bên trái.
   - Nhấp vào nút **New SSH key** (hoặc *Add an SSH key*).
   - Đặt một tiêu đề gợi nhớ trong ô Title (ví dụ: `Laptop-Dell-Kiet`), dán toàn bộ nội dung của tệp khóa công khai `~/.ssh/id_rsa.pub` (hoặc `id_ed25519.pub`) vào ô Key, rồi bấm **Add SSH key**.

Từ thời điểm này, bạn có thể thực hiện clone, push và fetch mã nguồn qua giao thức SSH (`git@github.com:...`) mà không cần phải nhập mật khẩu mỗi lần thao tác.

### Mã truy cập cá nhân (Personal Access Tokens - PAT)
Nếu bạn kết nối với GitHub thông qua giao thức HTTPS, bạn không thể sử dụng mật khẩu tài khoản trực tiếp trên dòng lệnh Git (kể từ tháng 8 năm 2021). Thay vào đó, bạn phải tạo một **Personal Access Token (PAT)**:
- Đi đến **Settings -> Developer settings -> Personal access tokens**.
- Chọn phạm vi truy cập (Scope) tối thiểu cần thiết, ví dụ đánh dấu chọn `repo` để đọc/ghi kho mã nguồn.
- Sao chép chuỗi mã Token vừa sinh ra và lưu trữ an toàn (dùng làm mật khẩu khi Git hỏi qua cổng HTTPS).

### Ảnh đại diện (Avatar)
GitHub hỗ trợ bạn tải lên một bức ảnh đại diện cá nhân trong mục **Profile**. Bức ảnh này sẽ hiển thị bên cạnh tên người dùng của bạn ở mọi nơi bạn tương tác trên trang web (bình luận mã nguồn, commit, Pull Request, Issues). Nếu bạn đã đăng ký dịch vụ Gravatar bằng email của mình, GitHub sẽ tự động nhận diện ảnh đại diện đó.

### Địa chỉ Email (Email Addresses)
Cách thức GitHub ánh xạ các commit Git vào tài khoản người dùng của bạn là thông qua **địa chỉ Email**. Khi bạn thực hiện commit trên máy tính, Git sẽ ghi lại tên tác giả và email từ cấu hình:
```bash
git config --global user.name "Nguyen Van A"
git config --global user.email "a.nguyen@example.com"
```
Nếu bạn sử dụng nhiều email khác nhau trên các máy tính làm việc hoặc dự án khác nhau, bạn cần vào mục **Emails** trong phần Settings của GitHub và thêm tất cả các địa chỉ email đó vào. Khi đó, GitHub sẽ tự động liên kết mọi commit có chứa các email này về đúng trang hồ sơ của bạn. Bạn cũng có thể tích chọn *Keep my email addresses private* để ẩn email cá nhân khi push mã nguồn.

### Xác thực hai yếu tố (Two Factor Authentication - 2FA)
Để bảo mật tài khoản ở mức cao nhất, bạn nên bật tính năng xác thực hai yếu tố tại mục **Password and authentication** (hoặc tab *Security*). Khi bật 2FA, mỗi lần đăng nhập vào website GitHub, ngoài mật khẩu bạn sẽ cần nhập thêm mã số 6 chữ số sinh ra từ ứng dụng trên điện thoại (như Google Authenticator, Microsoft Authenticator) hoặc nhận qua SMS.

---

## 6.2 ĐÓNG GÓP VÀO MỘT DỰ ÁN (CONTRIBUTING TO A PROJECT)

Sau khi tài khoản đã sẵn sàng, hãy cùng tìm hiểu quy trình phổ biến nhất trên GitHub: **đóng góp mã nguồn cho một dự án của người khác** khi bạn không có quyền ghi (write access) trực tiếp.

```
       QUY TRÌNH FORK VÀ PULL REQUEST (GITHUB FLOW)
  ┌────────────────────────────────────────────────────────┐
  │ Kho gốc (Upstream): github.com/owner/project            │
  └──────────────────────────┬─────────────────────────────┘
                             │  Bấm nút "Fork"
                             ▼
  ┌────────────────────────────────────────────────────────┐
  │ Kho cá nhân (Origin): github.com/your-user/project     │
  └──────────┬─────────────────────────────────▲───────────┘
             │ git clone                       │ git push
             ▼                                 │
  ┌───────────────────────┐         ┌──────────┴───────────┐
  │ Máy trạm cục bộ       │ ──────> │ Nhánh tính năng mới  │
  │ (Local Workspace)     │         │ (Topic/Feature branch)│
  └───────────────────────┘         └──────────┬───────────┘
                                               │
                                     Mở Pull Request
                                               ▼
  ┌────────────────────────────────────────────────────────┐
  │ Thảo luận, Review code dòng lệnh, Merge vào nhánh chính │
  └────────────────────────────────────────────────────────┘
```

### Tạo bản sao Fork (Creating a Fork)
Nếu bạn muốn tham gia đóng góp cho một dự án hiện có mà bạn không nằm trong danh sách cộng tác viên có quyền ghi trực tiếp, GitHub sử dụng mô hình **Forking**:
1. Truy cập trang GitHub của dự án bạn muốn đóng góp.
2. Nhấp vào nút **Fork** ở góc trên cùng bên phải trang web.
3. Sau vài giây, GitHub sẽ tạo ra một bản sao chép hoàn chỉnh của kho chứa đó dưới không gian tên tài khoản cá nhân của bạn (`https://github.com/<your_username>/<project_name>`).
4. Tại kho Fork này, bạn có toàn quyền ghi (`push`). Bạn có thể tự do chỉnh sửa, thử nghiệm và gửi các thay đổi đề xuất ngược lại cho kho gốc thông qua **Pull Request (PR)**.

### Quy trình GitHub Flow (The GitHub Flow)
GitHub Flow là quy trình làm việc xoay quanh nhánh và Pull Request được thiết kế đơn giản, tinh gọn và hiệu quả:
1. Tạo một nhánh tính năng (topic branch) tách ra từ nhánh chính (`master` hoặc `main`).
2. Thực hiện các commit thay đổi trên nhánh đó.
3. Đẩy nhánh tính năng lên kho lưu trữ cá nhân của bạn trên GitHub.
4. Mở một **Pull Request** nhắm tới nhánh chính của kho gốc.
5. Thảo luận, tiếp thu phản hồi, tiếp tục commit bổ sung vào nhánh nếu cần.
6. Sau khi chủ dự án đồng ý, Pull Request sẽ được hợp nhất (merge) vào nhánh chính.

#### Ví dụ minh họa thực tế từng bước:
Giả sử ta muốn đóng góp vào dự án mã nguồn mở điều khiển vi điều khiển Arduino tên là `blink` của tác giả `schacon` (`https://github.com/schacon/blink`). Chương trình hiện tại làm đèn LED nhấp nháy với chu kỳ 1 giây, ta muốn cải tiến chu kỳ này thành 3 giây.

**Bước 1: Fork dự án về tài khoản cá nhân `tonychacon`**  
Bấm nút **Fork** trên giao diện GitHub. Sau đó ta có kho: `https://github.com/tonychacon/blink`.

**Bước 2: Clone kho về máy tính và tạo nhánh tính năng**
```bash
$ git clone https://github.com/tonychacon/blink
$ cd blink
$ git checkout -b slow-blink
```

**Bước 3: Chỉnh sửa mã nguồn và tạo commit**  
Mở tệp `blink.ino`, sửa tham số hàm `delay(1000)` thành `delay(3000)`:
```bash
$ git diff --word-diff
diff --git a/blink.ino b/blink.ino
index 68427f9..498b584 100644
--- a/blink.ino
+++ b/blink.ino
@@ -18,7 +18,7 @@ void setup() {
 void loop() {
   digitalWrite(led, HIGH);   // bật đèn LED
   [-delay(1000);-]{+delay(3000);+}               // chờ 3 giây thay vì 1 giây
   digitalWrite(led, LOW);    // tắt đèn LED
   [-delay(1000);-]{+delay(3000);+}               // chờ 3 giây
 }

$ git commit -a -m 'Change delay to 3 seconds'
[slow-blink 5ca50ac] Change delay to 3 seconds
 1 file changed, 2 insertions(+), 2 deletions(-)
```

**Bước 4: Đẩy nhánh tính năng lên kho GitHub cá nhân**
```bash
$ git push origin slow-blink
Counting objects: 5, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 340 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
To https://github.com/tonychacon/blink
 * [new branch]      slow-blink -> slow-blink
```

### Tạo Yêu cầu Kéo mã nguồn (Creating a Pull Request)
Sau khi đẩy nhánh lên, khi truy cập vào kho chứa trên GitHub, bạn sẽ thấy một thanh thông báo màu vàng xuất hiện kèm theo nút xanh lá cây: **Compare & pull request**.
1. Nhấp vào nút **Compare & pull request**.
2. Kiểm tra xem nhánh cơ sở (Base repository & branch, ví dụ `schacon/blink:master`) và nhánh so sánh (Head repository & branch, ví dụ `tonychacon/blink:slow-blink`) đã chính xác chưa.
3. Điền **Tiêu đề (Title)** và **Mô tả chi tiết (Description)** cho Pull Request. Giải thích rõ lý do bạn thực hiện thay đổi này và lợi ích của nó.
4. Bấm nút **Create pull request**.

Lúc này, chủ sở hữu của kho gốc (`schacon`) sẽ nhận được thông báo qua email và giao diện web rằng có một lập trình viên vừa đề xuất thay đổi.

### Thảo luận và Tinh chỉnh trên Pull Request (Iterating on a Pull Request)
Một trong những điểm mạnh nhất của GitHub là khả năng tương tác trực tuyến trên từng dòng mã (Inline Code Review):
- Người duyệt mã (maintainer) có thể mở tab **Files changed**, di chuột vào bất kỳ dòng mã nào trong bản so sánh (unified diff) và bấm vào dấu cộng xanh để để lại lời nhận xét.
- Ví dụ: Maintainer nhận xét: *"Bạn có thể đổi tên biến chu kỳ trễ thành một hằng số `DELAY_TIME` ở đầu tệp để sau này dễ bảo trì hơn không?"*

Khi nhận được góp ý, người đóng góp không cần phải đóng PR cũ hay tạo PR mới! Quy trình sửa đổi vô cùng đơn giản:
1. Mở mã nguồn trên máy trạm cục bộ, chỉnh sửa tệp tin theo đúng góp ý.
2. Tạo một commit mới trên chính nhánh `slow-blink`.
3. Đẩy commit đó lên GitHub:
   ```bash
   $ git commit -a -m 'Define constant for delay time'
   $ git push origin slow-blink
   ```
GitHub sẽ **tự động phát hiện các commit mới và cập nhật thẳng vào Pull Request đang mở**! Mọi người có thể tiếp tục thảo luận cho đến khi hoàn toàn hài lòng.

### Xử lý xung đột khi Pull Request không thể trộn sạch
Nếu trong quá trình bạn phát triển nhánh tính năng, nhánh chính của kho gốc đã có những commit mới làm thay đổi cùng những dòng mã bạn vừa sửa, GitHub sẽ hiển thị cảnh báo: **This branch has conflicts that must be resolved** (Nút Merge sẽ bị khóa).

Để giải quyết tình huống này từ máy cá nhân:
1. Thêm kho gốc làm remote thứ hai (thường đặt tên là `upstream`):
   ```bash
   $ git remote add upstream https://github.com/schacon/blink
   $ git fetch upstream
   ```
2. Hòa trộn nhánh chính của kho gốc vào nhánh tính năng của bạn:
   ```bash
   $ git merge upstream/master
   ```
   *(Hoặc bạn có thể dùng `git rebase upstream/master` nếu muốn lịch sử commit thẳng thớm)*.
3. Xử lý các dấu hiệu xung đột (`<<<<<<<`, `=======`, `>>>>>>>`) trong các tệp mã nguồn.
4. Đánh dấu đã giải quyết và commit:
   ```bash
   $ git add blink.ino
   $ git commit
   $ git push origin slow-blink
   ```
Ngay sau khi push xong, thông báo xung đột trên trang Pull Request của GitHub sẽ biến mất, hiển thị thanh xanh báo hiệu sẵn sàng để merge.

### Cú pháp Markdown đặc thù của GitHub (GitHub Flavored Markdown - GFM)
Khi viết bình luận trong Issue, Pull Request hoặc viết tài liệu, GitHub mở rộng chuẩn Markdown thông thường bằng nhiều tính năng mạnh mẽ:

1. **Danh sách tác vụ (Task Lists):**
   ```markdown
   - [x] Đổi giá trị delay từ 1000 sang 3000
   - [ ] Đặt hằng số DELAY_TIME
   - [ ] Biên dịch thử trên mạch Arduino Uno
   ```
   GitHub sẽ hiển thị thành các ô checkbox có thể tích chọn trực tiếp trên trình duyệt, đồng thời hiển thị tiến độ (ví dụ: `1 of 3 tasks completed`) ngoài trang danh sách PR.

2. **Khối mã nguồn và tô màu cú pháp (Fenced Code Blocks):**
   Sử dụng ba dấu backtick kèm tên ngôn ngữ:
   ````markdown
   ```c
   #define DELAY_TIME 3000
   void loop() {
       digitalWrite(led, HIGH);
       delay(DELAY_TIME);
   }
   ```
   ````

3. **Trích dẫn có chọn lọc (Quoting):**
   Sử dụng ký tự `>` ở đầu dòng hoặc bôi đen văn bản trong bình luận của người khác rồi gõ phím `R` trên bàn phím để tự động trích dẫn.

4. **Biểu tượng cảm xúc (Emoji):**
   Gõ dấu `:` kèm tên biểu tượng, ví dụ `:thumbsup:` (:thumbsup:), `:+1:`, `:sparkles:`.

5. **Kéo thả hình ảnh (Drag & Drop Images):**
   Bạn chỉ cần kéo tệp ảnh từ máy tính thả trực tiếp vào ô bình luận, GitHub sẽ tự động upload ảnh lên máy chủ đám mây và chèn thẻ Markdown tương ứng.

6. **Tự động liên kết tham chiếu (Auto-linking):**
   - Viết `#42` sẽ tự động tạo liên kết đến Issue hoặc Pull Request số 42 trong cùng kho chứa.
   - Viết `owner/repo#42` để liên kết tới Issue của một kho chứa khác.
   - Viết SHA commit (ví dụ `5ca50ac`) sẽ tự động liên kết tới trang xem chi tiết commit đó.
   - Các từ khóa tự động đóng Issue: Nếu bạn ghi trong mô tả PR các cụm từ như `Fixes #12`, `Closes #12`, hoặc `Resolves #12`, khi Pull Request được merge vào nhánh chính, Issue số 12 sẽ **tự động chuyển sang trạng thái Closed**.

### Giữ cho kho lưu trữ của bạn luôn cập nhật
Sau khi nhánh của bạn đã được merge, bạn cần đồng bộ nhánh `master` cục bộ và kho Fork của mình để tiếp tục cho các tính năng tiếp theo:

**Cách 1: Kéo trực tiếp từ kho gốc (không cần lưu remote)**
```bash
$ git checkout master
$ git pull https://github.com/progit/progit2.git
$ git push origin master
```

**Cách 2: Cấu hình remote `upstream` lâu dài (khuyến nghị)**
```bash
$ git remote add upstream https://github.com/progit/progit2.git
$ git fetch upstream
$ git checkout master
$ git merge upstream/master
$ git push origin master
```

---

## 6.3 QUẢN TRỊ VÀ DUY TRÌ DỰ ÁN (MAINTAINING A PROJECT)

Phần này chuyển sang góc nhìn của người quản trị dự án: làm thế nào để tạo kho lưu trữ mới, phân quyền cộng tác viên và tiếp nhận các đóng góp mã nguồn từ người khác.

### Tạo một kho lưu trữ mới (Creating a New Repository)
Để tạo một kho chứa mới trên GitHub:
1. Bấm nút **New repository** (nút màu xanh) hoặc dấu cộng `+` ở góc trên cùng bên phải màn hình.
2. Đặt tên kho trong ô **Repository name** (ví dụ: `fade` hoặc `AspxDemo_NET481`).
3. Chọn chế độ hiển thị:
   - **Public:** Bất kỳ ai trên Internet đều có thể xem mã nguồn.
   - **Private:** Chỉ bạn và những người được bạn cấp quyền rõ ràng mới có thể xem và truy cập kho chứa.
4. Tùy chọn khởi tạo sẵn: Khởi tạo với tệp `README`, tệp `.gitignore` (chọn template phù hợp như *Visual Studio* cho dự án ASPX) và tệp giấy phép `LICENSE`.
5. Bấm **Create repository**.

Sau khi tạo, GitHub sẽ cung cấp các câu lệnh hướng dẫn đẩy một kho Git có sẵn từ máy tính lên:
```bash
git remote add origin https://github.com/<user>/AspxDemo_NET481.git
git branch -M main
git push -u origin main
```

### Thêm cộng tác viên (Adding Collaborators)
Nếu bạn làm việc theo nhóm (ví dụ nhóm đồ án), bạn không cần phải bắt các thành viên cùng nhóm fork kho chứa. Thay vào đó, bạn có thể cấp quyền ghi trực tiếp cho họ:
1. Vào tab **Settings** của repository $\rightarrow$ chọn mục **Collaborators** ở cột bên trái.
2. Nhập tên tài khoản GitHub hoặc địa chỉ email của thành viên vào ô tìm kiếm.
3. Nhấp vào **Add collaborator**.
4. Thành viên sẽ nhận được một email mời cộng tác; họ chỉ cần nhấp vào nút chấp nhận lời mời (Accept invitation) là có quyền push trực tiếp lên các nhánh của kho lưu trữ.

### Quản lý các Yêu cầu Kéo mã (Managing Pull Requests)
Khi có người mở một Pull Request gửi đến kho của bạn:

1. **Kiểm tra thông báo:** Bạn sẽ nhận được email và thông báo trên web.
2. **Thảo luận và Đánh giá mã:** Xem tab *Files changed*, nhận xét trực tiếp trên các dòng mã, yêu cầu sửa đổi nếu chưa đạt yêu cầu.
3. **Trộn mã nguồn (Merging):**
   - Nếu mọi thứ đều ổn, bạn chỉ cần bấm nút xanh **Merge pull request**, chọn kiểu merge (Create a merge commit, Squash and merge, hoặc Rebase and merge), sau đó bấm **Confirm merge**.
   - Nếu thay đổi không phù hợp, bạn có thể để lại lời giải thích lịch sự và bấm nút **Close pull request**.

#### Thao tác kiểm tra Pull Request tại dòng lệnh cục bộ
Nếu bạn muốn tải mã nguồn của Pull Request về máy tính để chạy thử, biên dịch hoặc gỡ lỗi trước khi quyết định merge trên web, bạn có thể lấy bản vá qua lệnh:
```bash
# Tải và áp dụng patch trực tiếp bằng cURL
$ curl https://github.com/tonychacon/fade/pull/1.patch | git am
```

### Các tham chiếu Pull Request đặc biệt (Pull Request Refs)
Mỗi khi có một Pull Request được tạo trên GitHub, hệ thống ngầm tạo ra một tập hợp các tham chiếu Git đặc biệt trên máy chủ có tiền tố:
`refs/pull/<PR_NUMBER>/head`

Bạn có thể kiểm tra các ref này bằng lệnh:
```bash
$ git ls-remote origin
```
Để tải toàn bộ các nhánh Pull Request về máy trạm thành các nhánh theo dõi từ xa, bạn có thể mở tệp cấu hình `.git/config` và bổ sung thêm một dòng `fetch` dưới mục `[remote "origin"]`:
```ini
[remote "origin"]
    url = https://github.com/schacon/blink.git
    fetch = +refs/heads/*:refs/remotes/origin/*
    fetch = +refs/pull/*/head:refs/remotes/origin/pr/*
```
Khi chạy `git fetch`, toàn bộ các PR sẽ tự động được tải về dưới dạng `origin/pr/1`, `origin/pr/2`,... Bạn có thể dễ dàng chuyển sang kiểm tra mã của PR số 1 bằng lệnh:
```bash
$ git checkout origin/pr/1
```

### Đề cập và Hệ thống Thông báo (Mentions and Notifications)
GitHub cung cấp hệ thống thông báo đa kênh:
- Khi bạn gõ `@username` trong bất kỳ bình luận nào, người đó sẽ nhận được thông báo ngay lập tức và tự động được đăng ký theo dõi (subscribe) vào cuộc thảo luận đó.
- Nút **Watch** ở đầu trang kho lưu trữ:
  - *Not Watching:* Chỉ nhận thông báo khi có người `@mention` bạn hoặc khi bạn tham gia vào thảo luận.
  - *Watching:* Nhận thông báo về mọi Issue, Pull Request và bình luận phát sinh trong toàn bộ kho chứa.
  - *Ignoring:* Không nhận bất kỳ thông báo nào.
- Trung tâm thông báo (**Notification Center**) trên thanh điều hướng cho phép bạn đánh dấu đã đọc (check mark) hoặc tắt theo dõi (*Mute*) các chuỗi thảo luận không còn liên quan.

### Các tệp tin quy ước đặc biệt (Special Files)
GitHub tự động nhận diện và hiển thị giao diện tối ưu cho một số tệp tin đặc biệt đặt ở thư mục gốc của kho:
1. **`README` (`README.md`, `README.txt`):** Hiển thị ngay tại trang đích giới thiệu kho lưu trữ.
2. **`CONTRIBUTING` (`CONTRIBUTING.md`):** Khi ai đó chuẩn bị mở một Issue hoặc Pull Request, GitHub sẽ hiển thị liên kết tới tệp này nhắc nhở họ tuân thủ các quy tắc đóng góp của nhóm.
3. **`LICENSE` (`LICENSE.txt`):** Xác định rõ giấy phép sử dụng mã nguồn mở (MIT, Apache 2.0, GPLv3,...). GitHub sẽ phân tích và hiển thị nhãn giấy phép nổi bật ở thanh thông tin bên phải trang chủ kho chứa.

### Quản trị dự án (Project Administration)
Trong tab **Settings** của repository, bạn có các quyền quản trị nâng cao:
- **Đổi tên kho chứa (Renaming a Repository):** Đổi tên kho bất cứ lúc nào; GitHub sẽ tự động tạo chuyển hướng (redirect) từ đường dẫn cũ sang đường dẫn mới.
- **Thay đổi nhánh mặc định (Changing the Default Branch):** Đổi nhánh chính từ `master` sang `main` hoặc `develop`.
- **Chuyển quyền sở hữu (Transferring a Repository):** Chuyển giao kho chứa sang tài khoản cá nhân khác hoặc vào một Organization.
- **Xóa kho chứa (Deleting a Repository):** Vùng nguy hiểm (Danger Zone) yêu cầu nhập lại chính xác tên kho trước khi xóa vĩnh viễn.

---

## 6.4 QUẢN LÝ TỔ CHỨC (MANAGING AN ORGANIZATION)

Bên cạnh tài khoản cá nhân, GitHub cung cấp loại tài khoản **Tổ chức (Organizations)** dành cho các công ty, câu lạc bộ hoặc nhóm phát triển dự án lớn.

```
                     MÔ HÌNH TỔ CHỨC (ORGANIZATION)
  ┌─────────────────────────────────────────────────────────────┐
  │ Organization: @cong-ty-abc                                  │
  ├─────────────────────────────────────────────────────────────┤
  │ Nhóm thành viên (Teams):                                    │
  │   ├── @cong-ty-abc/frontend  ──> Quyền ghi kho `web-ui`     │
  │   ├── @cong-ty-abc/backend   ──> Quyền ghi kho `api-core`   │
  │   └── @cong-ty-abc/devops    ──> Quyền Admin hạ tầng CI/CD  │
  └─────────────────────────────────────────────────────────────┘
```

### Cơ bản về Tổ chức (Organization Basics)
- Tổ chức có không gian tên riêng (`https://github.com/<org_name>`).
- Cho phép nhiều người cùng giữ vai trò Quản trị viên (Owners) mà không cần chia sẻ chung một tài khoản đăng nhập cá nhân.
- Các kho chứa thuộc sở hữu của tổ chức thay vì gắn với tài khoản cá nhân của một cá nhân cụ thể.

### Nhóm làm việc (Teams)
Tính năng Teams cho phép quản trị viên phân nhóm thành viên và gắn quyền truy cập cụ thể cho từng kho chứa:
- Tạo nhóm (ví dụ: nhóm lập trình viên giao diện `frontend`, nhóm lập trình viên dịch vụ `backend`).
- Gán quyền truy cập kho theo từng cấp độ: **Read** (chỉ đọc), **Write** (đọc và đẩy mã), **Admin** (toàn quyền quản trị).
- Đề cập nhóm: Khi bạn viết `@org_name/team_name` trong bình luận, tất cả các thành viên trong nhóm đó sẽ đồng loạt nhận được thông báo.

### Nhật ký kiểm toán (Audit Log)
Tổ chức cung cấp trang **Audit log** lưu lại lịch sử chi tiết mọi hành vi quan trọng: ai đã thêm thành viên mới, ai đổi quyền truy cập kho, ai đã xóa nhánh hay xóa kho lưu trữ, giúp nâng cao tính minh bạch và an toàn thông tin.

---

## 6.5 VIẾT KỊCH BẢN TỰ ĐỘNG HÓA VỚI GITHUB (SCRIPTING GITHUB)

Để tích hợp GitHub vào các hệ sinh thái bên ngoài hoặc tự động hóa các thao tác thủ công, GitHub cung cấp hai cơ chế mạnh mẽ: **Webhooks** và **GitHub REST API**.

### Dịch vụ và Webhooks (Services and Webhooks)
Trong phần cài đặt kho chứa (mục **Webhooks**):
- **Webhooks:** Cho phép bạn cung cấp một địa chỉ URL máy chủ của bạn (Payload URL). Mỗi khi có sự kiện diễn ra trên GitHub (ví dụ sự kiện `push`, `pull_request`, `issues`), GitHub sẽ gửi một yêu cầu HTTP POST chứa toàn bộ thông tin chi tiết dưới dạng JSON tới máy chủ của bạn.

#### Ví dụ xây dựng máy chủ nhận Webhook bằng Ruby Sinatra
Đoạn mã sau lắng nghe sự kiện push từ GitHub và tự động gửi email thông báo nếu có người đẩy mã lên nhánh chính:
```ruby
require 'sinatra'
require 'json'
require 'mail'

post '/payload' do
  push = JSON.parse(request.body.read)
  repo_name = push['repository']['full_name']
  
  # Duyệt qua từng commit được đẩy lên
  push['commits'].each do |commit|
    puts "Commit mới từ #{commit['author']['name']}: #{commit['message']}"
    # Có thể gửi email, kích hoạt máy chủ build hoặc thông báo Slack
  end
  return 200
end
```

### Giao diện lập trình ứng dụng GitHub API (The GitHub API)
GitHub cung cấp hệ thống REST API v3 vô cùng phong phú tại địa chỉ `https://api.github.com`.

1. **Truy vấn thông tin cơ bản không cần xác thực:**
   ```bash
   $ curl https://api.github.com/users/schacon
   {
     "login": "schacon",
     "id": 7874698,
     "name": "Scott Chacon",
     "public_repos": 112
   }
   ```

2. **Xác thực và thực hiện hành động ghi (Tạo bình luận trên Issue):**
   Sử dụng Personal Access Token truyền qua Header `Authorization`:
   ```bash
   $ curl -H "Authorization: token YOUR_PERSONAL_ACCESS_TOKEN" \
          -H "Content-Type: application/json" \
          -d '{"body": "Cảm ơn bạn đã mở Pull Request! Chúng tôi sẽ đánh giá sớm."}' \
          https://api.github.com/repos/tonychacon/fade/issues/1/comments
   ```

3. **Cập nhật trạng thái kiểm thử Commit (Commit Status API):**
   Các hệ thống CI/CD bên ngoài sử dụng endpoint này để báo cho GitHub biết commit đó build thành công (xanh) hay thất bại (đỏ):
   ```bash
   $ curl -H "Authorization: token YOUR_TOKEN" \
          -H "Content-Type: application/json" \
          -d '{
                "state": "success",
                "target_url": "https://ci.example.com/build/123",
                "description": "MSBuild và Test pass 100%",
                "context": "continuous-integration/jenkins"
              }' \
          https://api.github.com/repos/tonychacon/fade/statuses/6dcb09b5b57875f334f61aebed695e2e4193db5e
   ```

---

## 6.6 TỔNG KẾT CHƯƠNG (SUMMARY)

Chúc mừng bạn! Đến đây bạn đã nắm vững toàn bộ các kiến thức cốt lõi để trở thành một người dùng GitHub thành thạo:
- Bạn biết cách tạo tài khoản, cấu hình khóa bảo mật SSH và mã truy cập an toàn.
- Bạn hiểu sâu sắc quy trình cộng tác phân tán **GitHub Flow**: từ việc Fork kho, tạo nhánh tính năng, mở Pull Request cho đến thảo luận và giải quyết xung đột mã nguồn.
- Bạn nắm rõ vai trò của người quản trị dự án: phân quyền cộng tác viên, quản lý và merge các Pull Request, tổ chức nhóm qua mô hình Organization.
- Bạn biết cách tận dụng Webhooks và GitHub API để tự động hóa các thao tác lặp lại và kết nối với các hệ thống phần mềm bên ngoài.

---

## PHỤ LỤC KỸ THUẬT: CẬP NHẬT HIỆN ĐẠI HÓA & ỨNG DỤNG TRONG HỌC PHẦN ASPX
*(Phần biên soạn bổ sung chuyên sâu của Người dịch dành cho sinh viên học phần ASPX .NET Framework 4.8.1)*

Mặc dù cuốn sách *Pro Git (2nd Edition)* cung cấp nền móng lý thuyết rất vững chắc, nhưng do được viết vào năm 2014, độc giả cần được trang bị các bước phát triển vượt bậc của GitHub trong giai đoạn 2020–2026:

### 1. Sự ra đời của GitHub Actions thay thế Webhook thủ công
Trong mục 6.5, sách hướng dẫn lập trình máy chủ Webhook riêng để tự động hóa. Ngày nay, **GitHub Actions** đã trở thành tiêu chuẩn công nghiệp được tích hợp sẵn:
- File cấu hình YAML đặt tại `.github/workflows/ci-aspx-481.yml`.
- Với học phần ASP.NET Web Forms (.NET Framework 4.8.1), bắt buộc sử dụng máy ảo runner `windows-latest` có cài sẵn MSBuild, NuGet và IIS:
  ```yaml
  name: CI ASPX NET481
  on:
    push:
      branches: [ main, develop ]
    pull_request:
      branches: [ main ]
  jobs:
    build:
      runs-on: windows-latest
      steps:
        - uses: actions/checkout@v4
        - uses: microsoft/setup-msbuild@v2
        - uses: nuget/setup-nuget@v2
        - name: Restore NuGet Packages
          run: nuget restore AspxDemo_NET481.sln
        - name: Build Solution
          run: msbuild AspxDemo_NET481.sln /p:Configuration=Release
  ```

### 2. Nâng cấp từ Projects cũ lên GitHub Projects v2
Tính năng Projects trong mục 6.3 của sách trước đây chỉ là các cột kéo thả thủ công. Hiện nay **Projects v2** cung cấp bảng tính dữ liệu (Table view), lộ trình thời gian (Roadmap/Gantt) và hệ thống **Built-in Workflows** tự động chuyển thẻ từ `In Progress` sang `Done` ngay khi Pull Request được merge.

### 3. Bộ giải pháp An ninh nâng cao (GitHub Advanced Security)
Ngày nay, các dự án thực tế bắt buộc cấu hình các chốt chặn an ninh:
- **Secret Scanning & Push Protection:** Tự động chặn đứng lệnh `git push` nếu phát hiện lập trình viên vô tình để lộ chuỗi kết nối CSDL SQL Server hoặc mật khẩu trong commit.
- **Dependabot:** Tự động phân tích các tệp `packages.config` của ứng dụng ASP.NET, cảnh báo nếu các thư viện NuGet bên thứ ba có lỗ hổng bảo mật đã biết.
- **CodeQL (SAST):** Bộ máy phân tích mã tĩnh quét tìm các lỗi lập trình nguy hiểm như SQL Injection, Cross-Site Scripting (XSS) ngay trên mã nguồn C#.

---

### BẢNG THUẬT NGỮ KỸ THUẬT ANH - VIỆT CHUẨN HÓA

| Thuật ngữ gốc (English) | Thuật ngữ dịch tiếng Việt | Giải thích ngắn gọn |
|:---|:---|:---|
| **Repository (Repo)** | Kho lưu trữ / Kho chứa | Thư mục chứa toàn bộ lịch sử commit, nhánh và metadata của dự án |
| **Commit** | Điểm lưu vết / Ghi nhận | Ảnh chụp nhanh (snapshot) toàn bộ trạng thái mã nguồn tại một thời điểm |
| **Branch** | Nhánh | Con trỏ di động trỏ tới một commit độc lập để phát triển tính năng |
| **Fork** | Bản sao kho chứa trên đám mây | Bản sao độc lập của một repo vào không gian tài khoản cá nhân |
| **Pull Request (PR)** | Yêu cầu kéo / trộn mã nguồn | Lời đề xuất hợp nhất các thay đổi từ nhánh này sang nhánh khác kèm thảo luận |
| **Merge** | Hợp nhất / Trộn | Quy trình tích hợp các thay đổi giữa hai nhánh vào nhau |
| **Merge Conflict** | Xung đột hòa trộn | Tình huống hai người cùng sửa đổi một dòng mã trên cùng một tệp |
| **Upstream** | Kho nguồn gốc | Kho chứa ban đầu mà bạn đã thực hiện thao tác fork |
| **Remote** | Máy chủ kho từ xa | Địa chỉ kho lưu trữ đặt trên máy chủ đám mây (ví dụ: `origin`) |
| **Issue** | Vấn đề / Phiếu công việc | Nơi theo dõi lỗi phần mềm, yêu cầu tính năng hoặc thảo luận kỹ thuật |
| **Code Review** | Đánh giá / Xét duyệt mã | Hoạt động đồng nghiệp đọc và nhận xét mã nguồn trước khi merge |
| **Webhooks** | Điểm móc nối sự kiện web | Cơ chế máy chủ GitHub tự động bắn HTTP POST khi có sự kiện |

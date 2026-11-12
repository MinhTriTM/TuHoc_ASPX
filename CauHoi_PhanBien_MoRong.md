# Ngân hàng câu hỏi phản biện mở rộng — GIT, GitHub, GitLab (ASPX .NET Framework 4.8.1)

> 30 câu chia 3 mảng đúng theo mục 5 của `PhanCong_Nhom3TV.md`. Mỗi câu có gợi ý trả lời ngắn 2-4 câu để thành viên học thuộc trước buổi bảo vệ.

## Cách dùng trong buổi hỏi đáp

| Mảng | Người trả lời chính | Câu |
|------|---------------------|-----|
| Git (local + internals) | TV1 | A1–A10 |
| GitHub + Actions | TV2 | B1–B10 |
| GitLab + so sánh + tình huống nhóm | TV3 | C1–C10 |

## Phần A — Git: 10 câu (TV1)

### Câu A1. `git pull` khác gì `git fetch + git merge`?

**Câu hỏi:** `git pull` khác gì `git fetch + git merge`? Khi nào nên dùng `git pull --rebase`?

**Gợi ý trả lời:** `git fetch` chỉ tải commit mới về remote-tracking branch mà không trộn code, còn `git pull` bằng `fetch` rồi `merge` ngay vào nhánh hiện tại. Vì vậy `fetch + merge` tách bạch giúp xem trước thay đổi bằng `git log origin/main` trước khi trộn. `git pull --rebase` nên dùng trên nhánh cá nhân để đặt commit của mình lên trên commit mới, giữ lịch sử thẳng thay vì sinh merge commit thừa.

### Câu A2. `git reset` có 3 chế độ nào?

**Câu hỏi:** `git reset --soft`, `--mixed`, `--hard` khác nhau thế nào? Trường hợp nào được phép dùng `--hard`?

**Gợi ý trả lời:** Cả 3 chế độ đều dời con trỏ nhánh về một commit, nhưng `--soft` giữ nguyên index và working tree, `--mixed` (mặc định) reset index nhưng giữ file đang sửa, còn `--hard` xóa cả thay đổi trong index lẫn working tree. Chỉ dùng `--hard` khi chắc chắn muốn vứt bỏ mọi thay đổi chưa commit trên nhánh cá nhân. Tuyệt đối không `--hard` rồi force-push nhánh dùng chung vì sẽ xóa mất commit của người khác.

### Câu A3. `merge`, `rebase`, `cherry-pick` chọn cái nào khi nào?

**Câu hỏi:** So sánh `merge`, `rebase`, `cherry-pick` và cho biết vì sao cấm rebase nhánh public?

**Gợi ý trả lời:** `merge` giữ đầy đủ lịch sử phân nhánh và phù hợp khi hợp nhất nhánh feature đã review xong. `rebase` viết lại lịch sử cho thẳng đẹp nên chỉ dùng trên nhánh cá nhân chưa ai pull, vì rebase nhánh public đổi SHA khiến đồng đội bị trùng và mất commit. `cherry-pick` chỉ chép đúng 1 commit sang nhánh khác, hữu ích khi cần lấy gấp một bản sửa lỗi từ `main` về nhánh release.

### Câu A4. blob, tree, commit trong Git là gì?

**Câu hỏi:** Giải thích blob, tree, commit và vì sao Git phát hiện được khi file bị đổi 1 byte?

**Gợi ý trả lời:** blob lưu nội dung một file, tree lưu cấu trúc cây thư mục gồm tên file và SHA của các blob, còn commit trỏ tới một tree kèm thông điệp, tác giả và commit cha. Mỗi object được đặt tên bằng SHA-1 của chính nội dung nên chỉ cần đổi 1 byte là SHA đổi hoàn toàn. Cơ chế content-addressable này giúp Git kiểm tra toàn vẹn mọi commit chỉ bằng cách so sánh SHA.

### Câu A5. Vì sao `.gitignore` không có tác dụng với file đã commit?

**Câu hỏi:** Thêm `Web.config` vào `.gitignore` nhưng Git vẫn theo dõi thay đổi, vì sao và xử trí thế nào bằng `git rm --cached`?

**Gợi ý trả lời:** `.gitignore` chỉ áp dụng cho file chưa được tracked, còn file đã commit thì Git tiếp tục theo dõi bất kể ignore rule. Cách xử trí là chạy `git rm --cached Web.config` để gỡ file khỏi index nhưng giữ file trên đĩa, rồi commit thay đổi này. Sau đó mỗi máy giữ bản `Web.config` riêng từ `Web.template.config`, tránh đè connection string của nhau.

### Câu A6. `git revert` khác `git reset` thế nào?

**Câu hỏi:** Muốn hoàn tác một commit đã push lên `main` thì dùng `revert` hay `reset`? Vì sao?

**Gợi ý trả lời:** Dùng `git revert` vì nó tạo commit mới đảo ngược thay đổi, lịch sử cũ vẫn còn nên đồng đội pull về an toàn. `git reset` xóa commit khỏi lịch sử nên bắt buộc force-push và gây rắc rối cho người đã pull. Quy tắc nhớ là commit đã public thì chỉ `revert`, commit còn local trên nhánh riêng mới được `reset`.

### Câu A7. `git stash` dùng để làm gì?

**Câu hỏi:** Đang sửa dở form ASPX thì phải chuyển nhánh fix lỗi gấp, xử trí thế nào với `git stash`?

**Gợi ý trả lời:** Chạy `git stash -u` để cất tạm mọi thay đổi kể cả file mới, đưa working tree về sạch rồi chuyển nhánh fix lỗi. Sau khi commit bản fix, quay lại nhánh cũ và chạy `git stash pop` để lấy thay đổi ra làm tiếp. Nên đặt tên bằng `git stash push -m "dang sua Form DangKy"` để không nhầm khi có nhiều stash.

### Câu A8. Giải quyết conflict file `Web.config` thế nào?

**Câu hỏi:** Hai người cùng sửa connection string trong `Web.config` gây conflict, các bước giải quyết ra sao?

**Gợi ý trả lời:** Mở file, tìm 3 đoạn conflict giữa `<<<<<<<`, `=======`, `>>>>>>>` rồi giữ đúng một phiên bản connection string chuẩn cho môi trường dev. Sau đó chạy `git add Web.config` và `git commit` để hoàn tất merge, rồi build thử project ASPX để chắc chắn không vỡ config. Về lâu dài, tách connection string ra `Web.template.config` và file local không commit để tránh conflict lặp lại.

### Câu A9. `git tag` và `git branch` khác nhau thế nào?

**Câu hỏi:** Khi nộp đồ án môn học thì dùng tag hay branch để đánh dấu bản nộp? Vì sao?

**Gợi ý trả lời:** branch là con trỏ di chuyển theo mỗi commit mới, còn tag là mốc cố định gắn với đúng một commit. Vì vậy bản nộp bài dùng annotated tag như `git tag -a v1.0-nop -m "Ban nop lan 1"` để thầy cô luôn xem đúng commit đã chấm. Nhánh `main` vẫn tiếp tục phát triển sau đó mà không làm xê dịch tag nộp bài.

### Câu A10. `git reflog` cứu dữ liệu thế nào?

**Câu hỏi:** Lỡ `reset --hard` mất 2 commit chưa push, có lấy lại được không? Bằng cách nào?

**Gợi ý trả lời:** Lấy lại được nếu object chưa bị garbage collect, bằng cách xem `git reflog` để tìm SHA của commit trước khi reset. Sau đó chạy `git reset --hard <SHA>` hoặc tạo nhánh mới từ SHA đó để khôi phục công việc. Bài học là trước mọi lệnh nguy hiểm như `--hard` nên tạo nhánh dự phòng hoặc commit tạm để luôn có điểm quay lại.

## Phần B — GitHub + CI/CD: 10 câu (TV2)

### Câu B1. fork khác branch khi nào?

**Câu hỏi:** fork khác branch ở điểm nào? Vì sao bài tập nhóm 3 người dùng branch + PR thay vì fork?

**Gợi ý trả lời:** branch là nhánh trong cùng một repository nên chia sẻ chung Issues và Actions, còn fork là bản sao repository sang tài khoản khác, phù hợp đóng góp từ người ngoài. Nhóm 3 người cùng là collaborator nên dùng branch + Pull Request cho gọn, review nhanh và dùng chung một pipeline. fork chỉ cần khi làm bài tập cá nhân trên repo của thầy hoặc đóng góp cho dự án mã nguồn mở.

### Câu B2. protected branch chặn được lỗi gì?

**Câu hỏi:** protected branch kết hợp required review và status check chặn được những lỗi nào trong đồ án ASPX?

**Gợi ý trả lời:** protected branch cấm push thẳng lên `main` nên mọi thay đổi bắt buộc qua Pull Request có ít nhất 1 người review. required status check chặn merge khi GitHub Actions build `msbuild` còn đỏ, tránh gộp code vỡ. Nhờ đó lỗi quên file `.aspx`, sai `Web.config` hay thiếu reference đều bị pipeline bắt trước khi vào `main`.

### Câu B3. Vì sao build ASPX 4.8.1 cần Windows runner?

**Câu hỏi:** GitHub Actions build project ASP.NET Web Forms 4.8.1 cần runner nào? Vì sao không dùng `ubuntu-latest` + `dotnet build`?

**Gợi ý trả lời:** Project Web Forms 4.8.1 phụ thuộc .NET Framework chỉ có trên Windows và phải build bằng MSBuild kèm Visual Studio Build Tools. Vì vậy workflow phải dùng `runs-on: windows-latest` và action `setup-msbuild`. Image `ubuntu-latest` không có .NET Framework đầy đủ, còn `dotnet build` của .NET SDK hiện đại không biên dịch được project Web Forms dạng cũ.

### Câu B4. secrets trong Actions khác biến thường thế nào?

**Câu hỏi:** secrets trong GitHub Actions khác biến môi trường thường ở điểm nào? Connection string lưu ở đâu?

**Gợi ý trả lời:** secrets được mã hóa, che khi in log và chỉ workflow trên nhánh được phép mới đọc được, còn biến thường hiện rõ trong file YAML. Connection string thật phải lưu ở Settings, Secrets and variables, Actions và đọc qua `${{ secrets.DB_CONNECTION }}` trong bước transform config. Tuyệt đối không ghi connection string thật vào `Web.config` rồi commit lên repo.

### Câu B5. Cache NuGet packages trong pipeline ra sao?

**Câu hỏi:** Giải thích chiến lược cache NuGet packages để pipeline GitHub Actions chạy nhanh hơn.

**Gợi ý trả lời:** Dùng action `cache` với key băm từ `packages.config` hoặc `*.csproj` để lưu thư mục `~/.nuget/packages` giữa các lần chạy. Khi file project không đổi, job restore lấy package từ cache thay vì tải lại hàng trăm MB từ nuget.org. Nhờ đó thời gian pipeline giảm từ vài phút xuống còn khoảng 1 phút cho các lần build tiếp theo.

### Câu B6. Quy trình Pull Request chuẩn gồm bước nào?

**Câu hỏi:** Mô tả quy trình Pull Request chuẩn của nhóm từ lúc tạo nhánh đến khi merge.

**Gợi ý trả lời:** Quy trình gồm tạo nhánh `feature/ten-tinh-nang` từ `main`, commit theo Conventional Commits rồi push và mở PR kèm mô tả thay đổi. Ít nhất 1 thành viên review, Actions phải build xanh thì mới được merge bằng squash merge để lịch sử gọn. Sau khi merge thì xóa nhánh feature để repo không tồn đọng nhánh cũ.

### Câu B7. CODEOWNERS và rulesets làm gì?

**Câu hỏi:** File CODEOWNERS và rulesets trong GitHub có tác dụng gì cho đồ án nhóm?

**Gợi ý trả lời:** CODEOWNERS tự động gán đúng người review theo đường dẫn file, ví dụ TV1 review mọi thay đổi trong `BaoCao_LaTeX/`. rulesets là phiên bản mạnh hơn của protected branch, cho phép cấu hình rule theo pattern nhiều nhánh cùng lúc. Hai cơ chế này giúp nhóm nhỏ không sót review dù mỗi người phụ trách mảng khác nhau.

### Câu B8. Xử trí conflict trên Pull Request thế nào?

**Câu hỏi:** PR báo conflict ở `slide.tex`, các bước giải quyết chuẩn là gì?

**Gợi ý trả lời:** Pull `main` mới nhất về nhánh feature, mở `slide.tex` để chọn nội dung đúng giữa hai phía rồi commit bản gỡ conflict. Sau đó push lên đúng nhánh feature thì PR tự cập nhật và chuyển sang trạng thái mergeable. Không bao giờ bấm merge khi PR còn nhãn conflict vì GitHub sẽ trộn sai nội dung.

### Câu B9. Dependabot và secret scanning giúp gì?

**Câu hỏi:** Dependabot và secret scanning trong GitHub Advanced Security giúp gì cho project ASPX?

**Gợi ý trả lời:** Dependabot tự mở PR nâng cấp package NuGet khi phát hiện lỗ hổng, ví dụ nâng `Newtonsoft.Json` có CVE cũ. secret scanning quét toàn bộ lịch sử và báo ngay khi ai đó vô tình push connection string hay API key. Hai tính năng này đặc biệt hữu ích cho đồ án sinh viên vì nhóm thường quên cập nhật thư viện và kiểm tra secret.

### Câu B10. Viết workflow Actions tối thiểu cho ASPX 4.8.1 gồm bước nào?

**Câu hỏi:** Một workflow GitHub Actions tối thiểu để build project ASPX 4.8.1 gồm những bước nào?

**Gợi ý trả lời:** Workflow gồm 4 bước là checkout code, setup MSBuild, restore NuGet bằng `nuget restore`, rồi build bằng `msbuild /p:Configuration=Release`. Trigger đặt cho sự kiện `push` và `pull_request` lên `main` để mỗi PR đều được kiểm tra. Có thể thêm bước upload artifact file publish để thầy cô tải bản build về chạy thử.

## Phần C — GitLab, so sánh và tình huống nhóm: 10 câu (TV3)

### Câu C1. Merge Request khác Pull Request ở điểm nào?

**Câu hỏi:** Merge Request của GitLab khác Pull Request của GitHub ở những điểm nào?

**Gợi ý trả lời:** Về bản chất cả hai đều là đề xuất trộn code kèm review, nhưng GitLab gọi là Merge Request và tích hợp sâu với Approval rules bắt buộc đủ số approve theo vai trò. GitLab còn có Merge trains cho phép xếp hàng nhiều MR chạy pipeline rồi merge tuần tự mà không chờ từng cái. Ngoài ra MR của GitLab gắn chặt với Issue cùng project nên truy vết yêu cầu tới code dễ hơn mô hình repo rời của GitHub.

### Câu C2. `.gitlab-ci.yml` gồm khối chính nào?

**Câu hỏi:** File `.gitlab-ci.yml` gồm những khối chính nào? `stages`, `jobs`, `artifacts`, `cache` dùng ra sao?

**Gợi ý trả lời:** File gồm `stages` định nghĩa thứ tự các giai đoạn như build, test, deploy; mỗi job gắn vào một stage và chạy trên runner có tag phù hợp. `artifacts` lưu file kết quả như thư mục publish để job sau hoặc người dùng tải về, còn `cache` lưu dữ liệu tái sử dụng như package NuGet giữa các pipeline. Sự khác biệt cốt lõi là artifacts đi xuôi theo pipeline còn cache đi ngang giữa các lần chạy.

### Câu C3. Vì sao GitLab CI cần Windows runner + MSBuild cho ASPX?

**Câu hỏi:** Vì sao build ASPX 4.8.1 trên GitLab cần Windows runner + MSBuild? Vẽ các stage của pipeline.

**Gợi ý trả lời:** Giống GitHub Actions, project Web Forms 4.8.1 chỉ biên dịch bằng MSBuild trên Windows nên job phải khai báo `tags: [windows]` để điều phối tới đúng runner. Pipeline gồm 3 stage là build với `msbuild /p:Configuration=Release`, test chạy unit test nếu có, và deploy lưu artifact publish. Nếu gửi job sang runner Linux mặc định thì job thất bại ngay vì thiếu MSBuild và .NET Framework.

### Câu C4. Approval rules trong GitLab là gì?

**Câu hỏi:** Approval rules trong GitLab hoạt động thế nào và nhóm 3 người nên cấu hình ra sao?

**Gợi ý trả lời:** Approval rules quy định MR cần bao nhiêu approve và của vai trò nào, ví dụ ít nhất 1 Maintainer mới được merge. Nhóm 3 người nên đặt rule yêu cầu 1 approve từ người khác mảng, chẳng hạn MR của TV2 phải do TV1 hoặc TV3 duyệt. Cách này ngăn tự merge code của mình và buộc mỗi mảng đều có người ngoài kiểm tra chéo.

### Câu C5. So sánh GitHub và GitLab theo 5 tiêu chí cho đồ án môn học?

**Câu hỏi:** So sánh GitHub và GitLab theo 5 tiêu chí quan trọng nhất với đồ án môn học ASPX.

**Gợi ý trả lời:** Về CI/CD thì cả hai đều build được ASPX trên Windows runner, nhưng GitLab tích hợp pipeline ngay trong MR còn GitHub tách Actions riêng. Về review code, GitHub PR quen thuộc và nhiều tài liệu, còn GitLab MR mạnh hơn nhờ Approval rules chi tiết. Về chi phí, cả hai gói miễn phí đều đủ cho nhóm sinh viên, riêng GitLab cho self-host miễn phí khi trường muốn tự quản trị. Về bảo mật, GitHub mạnh ở secret scanning còn GitLab mạnh ở kiểm soát quyền theo Group. Với đồ án môn học, chọn GitHub khi ưu tiên tài liệu và cộng đồng, chọn GitLab khi cần quản trị tập trung và pipeline gắn liền MR.

### Câu C6. Environments và Review Apps trong GitLab là gì?

**Câu hỏi:** Environments và Review Apps trong GitLab giúp nhóm demo ASPX thế nào?

**Gợi ý trả lời:** Environments định nghĩa các môi trường như staging và production, mỗi lần deploy đều ghi lại ai deploy commit nào để dễ rollback. Review Apps tự tạo một môi trường demo riêng cho mỗi MR, nhờ đó thầy cô xem thử đúng giao diện của nhánh đang review mà không cần pull code. Với nhóm ASPX, Review App giúp phản biện trực quan thay vì chỉ đọc diff code.

### Câu C7. Self-hosted GitLab khi nào đáng dùng?

**Câu hỏi:** Khi nào nên dùng GitLab self-hosted thay vì GitLab SaaS hoặc GitHub cho đồ án?

**Gợi ý trả lời:** Self-hosted phù hợp khi trường yêu cầu dữ liệu ở máy chủ nội bộ hoặc cần tùy biến runner Windows cấu hình mạnh riêng. Tuy nhiên nhóm phải tự bảo trì máy chủ, cập nhật bản vá và sao lưu dữ liệu nên tốn công hơn bản SaaS. Với đồ án môn học thông thường không ràng buộc đặc biệt, bản SaaS miễn phí đủ dùng và đỡ gánh vận hành.

### Câu C8. Quy trình 3 người với `main/develop/feature` ra sao?

**Câu hỏi:** Mô tả quy trình nhánh `main/develop/feature` mà nhóm 3 người áp dụng cho repo ASPX demo.

**Gợi ý trả lời:** Nhánh `main` chỉ chứa code đã review và pipeline xanh, nhánh `develop` gom tính năng đang làm, mỗi người làm trên nhánh `feature/ten-viec` của mình. TV1 làm `.gitignore` và lịch sử mẫu, TV2 làm workflow GitHub Actions, TV3 làm pipeline GitLab rồi lần lượt gộp qua PR hoặc MR. Cuối mỗi tuần gộp `develop` vào `main` và gắn tag như `v0.2-tuan1` để đánh dấu mốc nộp.

### Câu C9. Lộ connection string lên public repo thì xử trí từng bước?

**Câu hỏi:** Một thành viên push `Web.config` chứa connection string thật lên repo public, xử trí từng bước thế nào?

**Gợi ý trả lời:** Bước 1 là đổi ngay mật khẩu database vì secret đã lộ coi như mất, không chỉ xóa commit. Bước 2 là gỡ secret khỏi lịch sử bằng `git filter-repo` hoặc BFG rồi force-push, đồng thời thu hồi mọi bản fork nếu có. Bước 3 là chuyển connection string sang secrets của Actions hoặc biến CI/CD của GitLab, bật secret scanning và họp nhóm rút kinh nghiệm về file mẫu `Web.template.config`.

### Câu C10. Bảng so sánh 20 tiêu chí gồm nhóm tiêu chí nào?

**Câu hỏi:** Bảng so sánh GitHub với GitLab trong báo cáo cần ít nhất 20 tiêu chí, nên chia thành nhóm nào?

**Gợi ý trả lời:** Bảng nên chia 5 nhóm là tổng quan gồm giá và self-host, quản lý code gồm repo và nhánh, CI/CD gồm runner Windows và artifacts, review gồm PR hoặc MR và approval, bảo mật gồm secret và quyền truy cập. Mỗi nhóm có 4-5 tiêu chí cụ thể kèm cột nhận xét gắn với project ASPX 4.8.1. Cách chia nhóm này giúp hội đồng theo dõi dễ và thấy rõ vì sao nhóm chọn từng nền tảng cho từng việc.

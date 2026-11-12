# Nhat ky commit mau — Repo AspxDemo_NET481 (Web Forms, .NET Framework 4.8.1)

> Nhom 3 thanh vien bat chuoc dung mau nay: 3 nhanh feature merge vao develop roi merge vao main. Moi commit tuan thu Conventional Commits, pham vi gan voi file ASPX that.

## 1. Quy uoc message (bat buoc)

| Tien to | Dung khi | Vi du that trong repo |
|---|---|---|
| `feat:` | Them chuc nang/trang moi | `feat(auth): them form DangNhap.aspx + kiem tra MSSV` |
| `fix:` | Sua loi | `fix(webconfig): sua connection string bi sai ten server` |
| `docs:` | Tai lieu, bao cao, slide | `docs(baocao): bo sung muc 7.3 lich su commit mau` |
| `ci:` | Pipeline GitHub/GitLab | `ci(actions): them job msbuild cho ASPX 4.8.1` |
| `style:` | Dinh dang, CSS, master page | `style(site): can le form tren Site.Master` |
| `refactor:` | Restructure khong doi hanh vi | `refactor(dal): tach lop DocSinhVien khoi code-behind` |
| `test:` | Them/sua test | `test(login): them case mat khau rong` |
| `chore:` | Linh tinh, gitignore, clean | `chore(git): chuan hoa .gitignore cho ASP.NET` |

Quy tac: mot commit mot viec, tieng Viet khong dau trong message, ten file ASPX viet hoa chu cai dau.

## 2. Do thi lich su mau: 20 commit, 3 nhanh feature

Chay `git log --graph --oneline --decorate -n 20` se thay cau truc tuong tu:

```text
* e7f2a91 (HEAD -> main, tag: v1.0) docs(slide): chot slide Q&A + trang phan cong TV1/TV2/TV3
* b81c4e0 docs(baocao): gan link repo GitHub + GitLab va anh pipeline vao muc 7
*   9f3a2c1 merge: phat hanh v1.0 tu develop (bao cao + slide + demo ASPX)
|\
| *   7e1b940 (develop) merge: gop feature/gitlab-ci vao develop (pipeline GitLab xanh)
| |\
| | * 4d2aa10 ci(gitlab): them stages build-test-package cho ASPX 4.8.1
| | * 31c8b77 ci(gitlab): them Windows runner + msbuild + cache NuGet
| | * 0a94e2d docs(gitlab): them trang SoSanh.aspx muc GitHub doi chieu GitLab
| * | 8c5d311 merge: gop feature/github-actions vao develop (Actions xanh)
| |\ \
| | |/
| | * 6f0e9c4 ci(actions): them job msbuild + vstest tren windows-2022
| | * 55a1d20 feat(trangchu): them LienHe.aspx + validation so dien thoai
| | * 19b7e42 fix(webconfig): tach connection string ra Secret, them transform
| * | 2b6f0a9 merge: gop feature/dang-nhap vao develop (review TV2, TV3 approve)
| |\ \
| | |/
| | * a41c8d3 test(login): them 3 case NUnit cho DangNhap.aspx.cs
| | * c07e1f2 style(site): can le form login tren Site.Master
| | * 9d22b60 feat(auth): them DangNhap.aspx + DangKy.aspx + code-behind
| | * 77e4a15 refactor(dal): tach SinhVienDB khoi Default.aspx.cs
| | * 5b3a991 feat(chung): tao Site.Master + Default.aspx + GioiThieu.aspx
| * 3e8f0aa chore(git): chuan hoa .gitignore ASP.NET + README bien dich LaTeX
| * 1c2d4e7 docs(phancong): them PhanCong_Nhom3TV.md + de cuong 8 chuong
| * 0f1a9b2 feat(khoitao): khoi tao solution AspxDemo_NET481 Web Forms 4.8.1
```

Giai thich nhanh:

| Nhanh | Nguoi | Commit thuoc nhanh | Merge vao dau |
|---|---|---|---|
| `feature/dang-nhap` | TV1 | 5 commit tu `5b3a991` den `a41c8d3` | `develop` tai `2b6f0a9` |
| `feature/github-actions` | TV2 | 3 commit tu `19b7e42` den `6f0e9c4` | `develop` tai `8c5d311` |
| `feature/gitlab-ci` | TV3 | 3 commit tu `0a94e2d` den `4d2aa10` | `develop` tai `7e1b940` |
| `develop` | Ca nhom | 3 commit goc + 3 commit merge | `main` tai `9f3a2c1`, them 2 commit `docs` |

## 3. Cach doc do thi (doi chieu nhanh voi commit)

- Doc tu duoi len: 3 commit goc tren `develop`, sau do lan luot 3 cum feature.
- Moi cum feature co day du `feat/fix/style/test/ci`, ten file ASPX nam ngay trong message.
- 3 commit `merge:` vao `develop`, 1 commit `merge:` len `main`, roi 2 commit `docs:` chot bai.
- Tong cong: 20 dong commit trong khoi `log --graph` muc 2, dem du 20 dau `*`.

## 4. Mau mo ta PR/MR (copy khung nay khi tao PR that)

### 4.1. PR-01: Trang dang nhap (TV1 nho TV2 review)

Tieu de: `feat(auth): them DangNhap.aspx + DangKy.aspx (PR tu feature/dang-nhap vao develop)`

Muc dich: co trang dang nhap chay duoc cho demo Git, lam nen cho phan phan quyen xem diem.

Thay doi chinh:

- Them `DangNhap.aspx`, `DangNhap.aspx.cs`, `DangKy.aspx`, `DangKy.aspx.cs`.
- Tach lop `SinhVienDB` ra `App_Code/SinhVienDB.cs`, bo doc truc tiep trong code-behind.
- Can le form tren `Site.Master`, them `RequiredFieldValidator` cho MSSV va mat khau.

Checklist test:

- [x] Mo `/DangNhap.aspx`, bo trong mat khau thay bao loi tieng Viet.
- [x] Nhap MSSV `SV001` + mat khau dung thi chuyen sang `Default.aspx`.
- [x] Build local `msbuild AspxDemo_NET481.sln /p:Configuration=Release` khong loi.
- [x] Chay 3 case `Tests/LoginTests.cs` deu pass.

Pipeline: GitHub Actions `ci-aspx-481` xanh (build 2m10s, test 3/3 pass). Anh chup man hinh pipeline dinh kem duoi.

Reviewers: `@TV2` (review code-behind), `@TV3` (review conflict voi `SoSanh.aspx`).

### 4.2. PR-02: GitHub Actions cho ASPX 4.8.1 (TV2 nho TV1 review)

Tieu de: `ci(actions): build msbuild + test ASPX 4.8.1 tren windows-2022`

Muc dich: moi PR vao `develop` deu duoc build that, chan loi bien dich truoc khi merge.

Thay doi chinh:

- Them `.github/workflows/ci-aspx-481.yml`: restore NuGet, msbuild Release, vstest, upload artifact.
- Sua `Web.config` + `Web.Release.config`: doc connection string tu Secret `DB_CONN`.
- Them `LienHe.aspx` lam trang test validation so dien thoai.

Checklist test:

- [x] Day nhanh len, Actions tu chay va bao xanh.
- [x] Thu sua sai mot dong trong `LienHe.aspx.cs`, Actions bao do dung nhu mong doi.
- [x] Kiem tra artifact `aspx-package.zip` tai ve duoc va co `bin/AspxDemo.dll`.
- [x] Secret `DB_CONN` khong lo trong log (kiem tra log tho).

Pipeline: Actions xanh 2 lan lien tiep. Anh chup man hinh tab Actions dinh kem.

Reviewers: `@TV1` (review Web.config transform), `@TV3` (doi chieu voi `.gitlab-ci.yml`).

### 4.3. MR-03: GitLab CI + trang so sanh (TV3 nho TV2 approve)

Tieu de: `ci(gitlab): pipeline Windows runner + trang SoSanh.aspx`

Muc dich: mirror sang GitLab van build duoc, co du lieu that cho chuong 5 va chuong 6.

Thay doi chinh:

- Them `.gitlab-ci.yml` voi 3 stage `build`, `test`, `package` chay tren Windows runner.
- Them `SoSanh.aspx` hien thi bang 20 tieu chi GitHub doi chieu GitLab.
- Them cache NuGet theo `packages.config` de giam 40% thoi gian pipeline.

Checklist test:

- [x] MR tu `feature/gitlab-ci` sang `develop`, can 1 approve cua TV2.
- [x] Pipeline GitLab xanh ca 3 stage, job `package` sinh duoc artifact.
- [x] Mo `/SoSanh.aspx` tren IIS Express thay du 20 dong tieu chi.
- [x] Khong commit de file `bin/`, `obj/`, `.vs/` (kiem tra Files changed).

Pipeline: GitLab pipeline `#87` xanh. Anh chup man hinh pipeline dinh kem.

Reviewers: `@TV2` (approve bat buoc theo Approval rule), `@TV1` (review cau truc bang).

## 5. Mau review comment (khen + yeu cau sua + goi y code)

### Comment 1 — Khen cau truc, nho tach ham

> Lam tot: tach `SinhVienDB` ra khoi code-behind giup `DangNhap.aspx.cs` gon hon han.
> Nho sua: ham `KiemTraDangNhap` dang dai 45 dong, tach rieng phan doc DB va phan kiem tra mat khau.
> Goi y:

```csharp
// DangNhap.aspx.cs — tach thanh 2 ham nho
protected void btnDangNhap_Click(object sender, EventArgs e)
{
    var sv = SinhVienDB.TimTheoMSSV(txtMSSV.Text.Trim());
    if (sv == null || !SinhVienDB.KiemTraMatKhau(sv, txtMatKhau.Text))
    {
        lblLoi.Text = "MSSV hoac mat khau chua dung.";
        return;
    }
    Response.Redirect("~/Default.aspx");
}
```

### Comment 2 — Bat loi bao mat Web.config

> Khen: dung `Web.Release.config` de transform la dung huong CI that.
> Bat buoc sua: file `Web.config` van con connection string that `Server=MAY-TV2;Pwd=123456`. Xoa ngay, doc tu bien moi truong.
> Goi y:

```csharp
// Doc connection string an toan trong SinhVienDB.cs
var connStr = System.Environment.GetEnvironmentVariable("DB_CONN");
if (string.IsNullOrEmpty(connStr))
{
    throw new InvalidOperationException("Thieu bien moi truong DB_CONN.");
}
```

### Comment 3 — Yeu cau them validator cho LienHe.aspx

> Khen: trang `LienHe.aspx` bo cuc sach, nhan tieng Viet ro rang.
> Nho sua: thieu `RegularExpressionValidator` cho so dien thoai 10 so dau 0, hien tai nhap chu van submit duoc.
> Goi y:

```aspx
<asp:TextBox ID="txtSDT" runat="server" MaxLength="10" />
<asp:RegularExpressionValidator ID="valSDT" runat="server"
    ControlToValidate="txtSDT" ErrorMessage="So dien thoai phai co 10 so, bat dau bang 0."
    ValidationExpression="^0\d{9}$" Display="Dynamic" ForeColor="Red" />
```

### Comment 4 — Yeu cau sua pipeline msbuild

> Khen: pipeline viet gon, co cache NuGet nen chay nhanh hon ban cu 1 phut.
> Nho sua: job build dang dung `ubuntu-latest` nen `msbuild` khong ton tai. ASPX 4.8.1 bat buoc Windows.
> Goi y:

```yaml
jobs:
  build:
    runs-on: windows-2022
    steps:
      - uses: actions/checkout@v4
      - name: Setup MSBuild
        uses: microsoft/setup-msbuild@v2
      - name: Build ASPX 4.8.1
        run: msbuild AspxDemo_NET481.sln /p:Configuration=Release
```

### Comment 5 — Khen trang so sanh, nho sua du lieu

> Khen: bang `SoSanh.aspx` du 20 tieu chi, cot nao cung co vi du ASPX cu the.
> Nho sua truoc khi merge: dong 14 ghi GitLab khong co Pages la sai, doi thanh ho tro GitLab Pages.
> Goi y sua ngay tren dong HTML:

```aspx
<tr><td>14</td><td>Dang tai lieu mon hoc</td><td>GitHub Pages</td><td>GitLab Pages</td></tr>
```
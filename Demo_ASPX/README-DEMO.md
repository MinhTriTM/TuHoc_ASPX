# README Demo: Dung repo AspxDemo_NET481 tu con so 0

> Du an mau ASP.NET Web Forms chay .NET Framework 4.8.1, phuc vu bai trinh bay
> mon ASPX ve GIT - GitHub - GitLab (nhom 3 thanh vien). Lam theo dung 12 buoc
> duoi day de co repo co lich su Git that, CI xanh tren ca 2 nen tang.

## 1. Muc tieu

- Co solution `AspxDemo_NET481.sln` bien dich duoc bang MSBuild tren Windows.
- Co 2 trang Web Forms chay duoc: `Default.aspx` va `Login.aspx`.
- Co lich su Git dung quy uoc Conventional Commits, mo hinh `main/develop/feature`.
- Co CI xanh tren GitHub Actions va GitLab CI (Windows runner).

## 2. Yeu cau tien quyet

| # | Thanh phan | Phien ban toi thieu | Cach kiem tra |
|---|-----------|---------------------|---------------|
| 1 | Visual Studio 2022 | 17.8, workload ASP.NET | Mo VS, xem Help > About |
| 2 | .NET Framework 4.8.1 | Developer Pack | `reg query "HKLM\SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full" /v Release` |
| 3 | Git for Windows | 2.40+ | `git --version` |
| 4 | Tai khoan GitHub | Mien phi | Dang nhap github.com thanh cong |
| 5 | Tai khoan GitLab | Mien phi (SaaS) | Dang nhap gitlab.com thanh cong |
| 6 | MSBuild | Theo VS2022 | `msbuild -version` trong Developer Prompt |

Cau hinh Git 1 lan duy nhat tren may:

```bat
git config --global user.name "Ho Ten"
git config --global user.email "mssv@ university.edu.vn"
git config --global init.defaultBranch main
git config --global core.autocrlf true
```

## 3. Muoi hai buoc dung repo

### Buoc 1. Tao solution Web Forms .NET Framework 4.8.1

1. Mo Visual Studio 2022, chon Create a new project.
2. Chon mau ASP.NET Web Application (.NET Framework), bam Next.
3. Dat ten project `AspxDemo_NET481`, chon Framework `4.8.1`, bam Create.
4. Chon mau Web Forms, bo dau HTTPS va Docker, bam Create.
5. Nhan Ctrl+Shift+B de bien dich thu; phai thay `Build succeeded`.

### Buoc 2. Them trang Default.aspx

1. Chuot phai project, chon Add > Web Form, dat ten `Default.aspx`.
2. Thay noi dung phan body bang dong chao don gian:

```aspx
<h2>Chao mung den voi AspxDemo_NET481 (.NET 4.8.1)</h2>
<asp:Label ID="lblTime" runat="server" Text="Dong ho se hien thi o day" />
```

3. Trong `Default.aspx.cs`, xu ly su kien `Page_Load` de hien thi gio he thong:

```csharp
protected void Page_Load(object sender, EventArgs e)
{
    if (!IsPostBack)
    {
        lblTime.Text = "Thoi gian hien tai: " + DateTime.Now.ToString("dd/MM/yyyy HH:mm:ss");
    }
}
```

4. Nhan F5, trang chu phai hien thi gio he thong.

### Buoc 3. Them trang Login.aspx

1. Chuot phai project, chon Add > Web Form, dat ten `Login.aspx`.
2. Them 2 o nhap va 1 nut don gian trong the form:

```aspx
<asp:TextBox ID="txtUser" runat="server" placeholder="Ten dang nhap" />
<asp:TextBox ID="txtPass" runat="server" TextMode="Password" placeholder="Mat khau" />
<asp:Button ID="btnLogin" runat="server" Text="Dang nhap" OnClick="btnLogin_Click" />
<asp:Label ID="lblMsg" runat="server" ForeColor="Red" />
```

3. Trong `Login.aspx.cs`, kiem tra tai khoan demo `admin/123456`:

```csharp
protected void btnLogin_Click(object sender, EventArgs e)
{
    if (txtUser.Text == "admin" && txtPass.Text == "123456")
    {
        lblMsg.ForeColor = System.Drawing.Color.Green;
        lblMsg.Text = "Dang nhap thanh cong. Chao admin!";
    }
    else
    {
        lblMsg.Text = "Sai tai khoan hoac mat khau demo.";
    }
}
```

4. Nhan F5, mo `/Login.aspx`, nhap `admin/123456`, phai thay thong bao thanh cong.

### Buoc 4. Tao file .gitignore chuan ASP.NET

1. Tai thu muc goc cua solution, tao file `.gitignore` voi noi dung toi thieu:

```gitignore
## Build ##
[Bb]in/
[Oo]bj/
[Tt]est[Rr]esult*/
[Bb]uild/
*.user
*.suo
.vs/
packages/
*.cache
```

2. Kiem tra bang lenh `git status`; thu muc `bin/`, `obj/`, `.vs/` khong duoc xuat hien.

### Buoc 5. Khoi tao Git va tao commit dau tien

```bash
cd AspxDemo_NET481
git init
git add .
git commit -m "feat: khoi tao solution Web Forms 4.8.1 voi Default va Login"
git log --oneline
```

- Ket qua mong doi: `git log` hien thi dung 1 commit tren nhanh `main`.

### Buoc 6. Tao nhanh develop tu main

```bash
git checkout -b develop
git push -u origin develop
```

- Tu nay, `main` chi nhan merge tu `develop` thong qua pull request.

### Buoc 7. Tao 3 nhanh feature cho 3 thanh vien

```bash
git checkout develop
git checkout -b feature/git-co-ban
git checkout develop
git checkout -b feature/github-actions
git checkout develop
git checkout -b feature/gitlab-ci
git branch
```

| Nhanh | Nguoi phu trach | Noi dung |
|-------|----------------|----------|
| `feature/git-co-ban` | TV1 | Hoan thien `.gitignore`, lich su commit mau |
| `feature/github-actions` | TV2 | Them file `.github/workflows/ci-aspx-481.yml` |
| `feature/gitlab-ci` | TV3 | Them file `.gitlab-ci.yml` |

### Buoc 8. Day code len GitHub

```bash
git remote add origin https://github.com/MinhTriTM/AspxDemo_NET481.git
git checkout main
git push -u origin main
git checkout develop
git push -u origin develop
git push --all origin
```

- Tao repo tren GitHub truoc, de che do Public, khong tich Add README.

### Buoc 9. Mirror repo sang GitLab

1. Tren GitLab, chon New project > Import project > Repo by URL.
2. Dan URL GitHub `https://github.com/MinhTriTM/AspxDemo_NET481.git`, dat ten project trung ten.
3. Sau khi import xong, them remote thu 2 tren may local:

```bash
git remote add gitlab https://gitlab.com/<ten-nhom>/AspxDemo_NET481.git
git fetch gitlab
git push gitlab --all
```

4. Bat Mirroring (Settings > Repository > Mirroring repositories) de GitLab tu dong keo tu GitHub.

### Buoc 10. Bat GitHub Actions cho ASPX 4.8.1

1. Tren nhanh `feature/github-actions`, tao file `.github/workflows/ci-aspx-481.yml`.
2. Noi dung pipeline dung Windows runner va MSBuild, chi tiet xem phu luc C.1 cua bao cao.
3. Mo pull request tu `feature/github-actions` vao `develop`, nho 1 ban review roi merge.
4. Vao tab Actions tren GitHub, cho job `build` chay xong.

### Buoc 11. Bat pipeline GitLab cho ASPX 4.8.1

1. Tren nhanh `feature/gitlab-ci`, tao file `.gitlab-ci.yml` dung tag `windows`.
2. Noi dung pipeline co 3 stage `restore/build/test`, chi tiet xem phu luc C.2 cua bao cao.
3. Mo merge request vao `develop`, bat Approval (can 1 approve), merge khi du dieu kien.
4. Vao menu CI/CD > Pipelines tren GitLab, theo doi job chay tren shared Windows runner.

### Buoc 12. Kiem tra CI xanh tren ca 2 nen tang

1. GitHub: tab Actions phai hien thi dau tich xanh cho commit moi nhat cua `develop`.
2. GitLab: menu CI/CD > Pipelines phai hien thi `passed` cho commit tuong ung.
3. Chup anh 2 man hinh pipeline xanh, dua vao Chuong 7 cua bao cao.
4. Merge `develop` vao `main` bang 1 pull request cuoi, gan tag `v1.0-demo`:

```bash
git checkout main
git merge develop
git tag -a v1.0-demo -m "Ban demo nop bai mon ASPX"
git push origin main --tags
```

## 4. Bang kiem tra cuoi truoc khi nop

| # | Muc kiem tra | Cach xac minh | Dat |
|---|-------------|---------------|-----|
| 1 | Solution bien dich sach bang MSBuild | `msbuild AspxDemo_NET481.sln /p:Configuration=Release` bao succeeded | [ ] |
| 2 | Du 2 trang Default.aspx va Login.aspx chay duoc | F5 tung trang, dang nhap demo thanh cong | [ ] |
| 3 | Lich su Git co main/develop/3 feature + tag | `git branch -a` va `git tag` hien thi day du | [ ] |
| 4 | GitHub Actions bao xanh | Tab Actions co dau tich xanh o commit moi nhat | [ ] |
| 5 | GitLab pipeline bao passed | Menu CI/CD > Pipelines hien thi passed | [ ] |

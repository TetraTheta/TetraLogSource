---
title: "[Visual Studio] UI 요소 숨기기"
slug: visual-studio-hide-ui-element
date: 2025-02-01T16:02:43+09:00
series:
#  - 
categories:
  - PIVOX
tags:
  - Visual Studio
images:
  - logo.webp
---

Visual Studio는 매우 훌륭한 IDE입니다만, 사소한 부분에서 부족한 점이 있습니다. 창 상단의 툴바를 고정할 수 없다거나, 특정 UI 요소를 숨길 수 없다거나 하는 것 말이죠.

이 글에서는 은근히 거슬리는 로그인 버튼과 피드백 버튼을 제거하는 방법을 알려드리겠습니다.

{{< gallery/image src="001" caption="우측 상단의 로그인 버튼과 피드백 버튼" >}}

# Visual Commander 설치

먼저 [Visual Commander](https://marketplace.visualstudio.com/items?itemName=SergeyVlasov.VisualCommander) 확장 패키지 설치가 필요합니다.

<link-preview url="https://marketplace.visualstudio.com/items?itemName=SergeyVlasov.VisualCommander" title="Visual Commander - Visual Studio Marketplace" desc="Extension for Visual Studio - Automate repetitive tasks in Visual Studio IDE. Reuse your existing Visual Studio macros or create new commands and extensions in C# or VB. Record and playback text editing macros." image="https://SergeyVlasov.gallerycdn.vsassets.io/extensions/sergeyvlasov/visualcommander/3.4.1/1738562624414/Microsoft.VisualStudio.Services.Icons.Default"></link-preview>

Visual Studio를 연 뒤, '확장 - 확장 관리' 메뉴를 눌러 확장 관리자를 엽니다.

{{< gallery/image src="002" >}}

검색창에 Visual Commander를 검색한 후, 해당 확장 패키지를 설치합니다. Visual Studio를 완전히 종료해야 확장 패키지가 실제로 설치되므로, Visual Studio를 종료한 후, 다시 시작합니다.

이제 Visual Studio를 다시 열면 '확장' 메뉴 아래 VCmd 메뉴가 새로 생긴 것을 확인할 수 있습니다.

# Extension 다운로드 및 불러오기

다음 두 파일을 다운로드합니다.

* [Hide Feedback in VS 2022.vcmd](https://www.mediafire.com/file/4zgh77rqnjtl2zf/Hide_Feedback_in_VS_2022.vcmd/file)
* [Hide Sign In in VS 2022.vcmd](https://www.mediafire.com/file/u0tds14h2ocyihk/Hide_Sign_In_in_VS_2022.vcmd/file)

{{< collapse heading="Hide Feedback in VS 2022.vcmd의 내용" >}}
```xml
<?xml version="1.0" encoding="utf-8"?>
<SerializableSnippets xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <commands />
  <extensions>
    <Snippet>
      <id>1</id>
      <name>Hide Feedback in VS 2022</name>
      <code>public class HideFeedback : VisualCommanderExt.IExtension {
  private System.Windows.Threading.DispatcherTimer timer;
  private string target = "FeedbackButton";
  
  public void SetSite(EnvDTE80.DTE2 DTE, Microsoft.VisualStudio.Shell.Package package) {
    timer = new System.Windows.Threading.DispatcherTimer();
    timer.Interval = System.TimeSpan.FromMilliseconds(1000);
    timer.Tick += OnTimer;
    if (!HideElement()) timer.Start();
  }
  
  public void Close() { timer.Stop(); }
  
  private void OnTimer(System.Object o, System.EventArgs a) {
    try { if (HideElement()) timer.Stop(); }
    catch (System.Exception e) {}
  }
  
  private bool HideElement() {
    System.Windows.FrameworkElement e = FindElement(System.Windows.Application.Current.MainWindow, target);
    if (e != null) {
      e.Visibility = System.Windows.Visibility.Collapsed;
      return true;
    }
    return false;
  }
  
  private System.Windows.FrameworkElement FindElement(System.Windows.Media.Visual v, string name) {
    if (v == null) return null;
    for (int i = 0; i &lt; System.Windows.Media.VisualTreeHelper.GetChildrenCount(v); ++i) {
      System.Windows.Media.Visual child = System.Windows.Media.VisualTreeHelper.GetChild(v, i) as System.Windows.Media.Visual;
      if (child != null) {
        System.Windows.FrameworkElement e = child as System.Windows.FrameworkElement;
        if (e != null &amp;&amp; e.Name == name) return e;
      }
      System.Windows.FrameworkElement result = FindElement(child, name);
      if (result != null) return result;
    }
    return null;
  }
}
</code>
      <referencedAssemblies />
      <type>Extension</type>
      <lang>CS</lang>
      <langVersion>v4.0</langVersion>
      <enabled>true</enabled>
      <includeDebugInformation>false</includeDebugInformation>
    </Snippet>
  </extensions>
  <commonCode />
</SerializableSnippets>
```
{{< /collapse >}}

{{< collapse heading="Hide Sign In in VS 2022.vcmd의 내용" >}}
```xml
<?xml version="1.0" encoding="utf-8"?>
<SerializableSnippets xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <commands />
  <extensions>
    <Snippet>
      <id>2</id>
      <name>Hide Sign in VS 2022</name>
      <code>public class HideSignIn : VisualCommanderExt.IExtension {
  private System.Windows.Threading.DispatcherTimer timer;
  private string target = "PART_TitleBarRightFrameControlContainer";
  
  public void SetSite(EnvDTE80.DTE2 DTE, Microsoft.VisualStudio.Shell.Package package) {
    timer = new System.Windows.Threading.DispatcherTimer();
    timer.Interval = System.TimeSpan.FromMilliseconds(1000);
    timer.Tick += OnTimer;
    if (!HideElement()) timer.Start();
  }

  public void Close() { timer.Stop(); }

  private void OnTimer(System.Object o, System.EventArgs a) {
    try { if (HideElement()) timer.Stop(); }
    catch (System.Exception e) {}
  }

  private bool HideElement() {
    System.Windows.FrameworkElement e = FindElement(System.Windows.Application.Current.MainWindow, target);
    if (e != null) {
      e.Visibility = System.Windows.Visibility.Collapsed;
      return true;
    }
    return false;
  }

  private System.Windows.FrameworkElement FindElement(System.Windows.Media.Visual v, string name) {
    if (v == null) return null;
    for (int i = 0; i &lt; System.Windows.Media.VisualTreeHelper.GetChildrenCount(v); ++i) {
      System.Windows.Media.Visual child = System.Windows.Media.VisualTreeHelper.GetChild(v, i) as System.Windows.Media.Visual;
      if (child != null) {
        System.Windows.FrameworkElement e = child as System.Windows.FrameworkElement;
        if (e != null &amp;&amp; e.Name == name) return e;
      }
      System.Windows.FrameworkElement result = FindElement(child, name);
      if (result != null) return result;
    }
    return null;
  }
}
</code>
      <referencedAssemblies />
      <type>Extension</type>
      <lang>CS</lang>
      <langVersion>v4.0</langVersion>
      <enabled>true</enabled>
      <includeDebugInformation>false</includeDebugInformation>
    </Snippet>
  </extensions>
  <commonCode />
</SerializableSnippets>
```
{{< /collapse >}}

'확장 - VCmd - Import'를 눌러 두 vcmd 파일을 불러옵니다. 각각 하나의 Extension을 등록합니다.

{{< gallery/image src="003" >}}

이제 Visual Studio를 재시작하면 로그인 버튼과 피드백 버튼이 사라진 걸 확인할 수 있습니다.

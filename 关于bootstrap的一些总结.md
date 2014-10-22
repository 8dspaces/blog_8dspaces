<link rel="stylesheet" href="http://yandex.st/highlightjs/8.0/styles/default.min.css">
<script src="http://yandex.st/highlightjs/8.0/highlight.min.js"></script>
<script>hljs.tabReplace = ' ';hljs.initHighlightingOnLoad();</script>

<link href="/Users/mickqi/Dropbox/my_books/static/bootstrap/css/bootstrap.min.css" rel="stylesheet"> 


##  关于BootStrap的一些总结   

`Bootstrap `是Twitter发布的一套优秀的前端框架，提供了快速构建前端页面的方式，实用优雅
大量现成的css, javascript控件可控选择 （BS JS 基于jQuery, 结合JQuery的控件，更加强大）


#### 排版 

+ 正常的 h1 ~ h6 
+ grid 控制  12  960px
   
      <div class = 'row'>
          <div class= 'span1…12'> </div>
          <div class= 'span4 offset1…12'> </div>
      </div>
      
+ hero-unit 

      <div class = 'hero-unit'>
          <h1>project title</h1>
          <p>This is description</p>
          <a class= 'btn btn-primary'> Get Start... </a>
      </div>
      
      
      
#### 导航条

+  navbar 标准

        div.navbar  navbar-fixed-top
            navbar-inner 
                container
                a.brand  project name
                ul.nav 
                    li> a > i.icon-*  
                form.navbar-form 
                dropdown 
+  navbar form 

        <form class="navbar-form pull-left">
          <input type="text" class="span2">
          <button type="submit" class="btn">Submit</button>
        </form>
        
+ search form 

        <form class="navbar-search pull-left">
          <input type="text" class="search-query" placeholder="Search">
        </form>
        
#### 导航

+  标签页 

        <ul class="nav nav-tabs">
          <li class="active">
            <a href="#">首页</a>
          </li>
          <li><a href="#">...</a></li>
          <li><a href="#">...</a></li>
        </ul>    
        
+  Pills 

        <ul class="nav nav-pills">
          <li class="active">
            <a href="#">首页</a>
          </li>
          <li><a href="#">...</a></li>
          <li><a href="#">...</a></li>
        </ul>
+ stacked 

        <ul class="nav nav-tabs nav-stacked">
          ...
        </ul>      
          
+ 导航列表

        <ul class="nav nav-list">
          <li class="nav-header">List header</li>
          <li class="active"><a href="#">首页</a></li>
          <li><a href="#">Library</a></li>
          ...
        </ul>   

+  navbar dropdown 

        <ul class="nav nav-tabs">
          <li class="dropdown">
            <a class="dropdown-toggle"
               data-toggle="dropdown"
               href="#">
                Dropdown
                <b class="caret"></b>
              </a>
            <ul class="dropdown-menu">
              <!-- links -->
            </ul>
          </li>
        </ul>
+ 标签页连动起来

为了让标签页可切换，需要在`.tab-content`中创建一个带有唯一ID的`.tab-pane`。

        <div class="tabbable"> <!-- Only required for left/right tabs -->
          <ul class="nav nav-tabs">
            <li class="active"><a href="#tab1" data-toggle="tab">Section 1</a></li>
            <li><a href="#tab2" data-toggle="tab">Section 2</a></li>
          </ul>
          <div class="tab-content">
            <div class="tab-pane active" id="tab1">
              <p>I'm in Section 1.</p>
            </div>
            <div class="tab-pane" id="tab2">
              <p>Howdy, I'm in Section 2.</p>
            </div>
          </div>
        </div>
             
#### btn-group 

`.btn` 通常是用于更好的表现`<a> `和 `<button> `页面元素。

    <div class="btn-group">
      <button class="btn">Left</button>
      <button class="btn">Middle</button>
      <button class="btn">Right</button>
    </div>
    
#### thumbnail 

    <ul class="thumbnails">
      <li class="span4">
        <div class="thumbnail">
          <img data-src="holder.js/300x200" alt="">
          <h3>Thumbnail label</h3>
          <p>Thumbnail caption...</p>
        </div>
      </li>
      ...
    </ul>

#### 分页

    <div class="pagination">
      <ul>
        <li><a href="#">Prev</a></li>
        <li><a href="#">1</a></li>
        <li><a href="#">2</a></li>
        <li><a href="#">3</a></li>
        <li><a href="#">4</a></li>
        <li><a href="#">5</a></li>
        <li><a href="#">Next</a></li>
      </ul>
    </div>

#### table

    <table class="table table-striped|table-bordered|table-condensed|table-hover">
      …
    </table>

#### 面包屑

    <ul class="breadcrumb">
      <li><a href="#">首页</a> <span class="divider">/</span></li>
     <li><a href="#">Library</a> <span class="divider">/</span></li>
      <li class="active">Data</li>
    </ul>

#### form相关

+  select option 

        multiple="multiple"
       
+  textarea
 
        <textarea row ='5'> </textarea>
+ 单选复选框

        <label class="checkbox">
          <input type="checkbox" value="">
          Option one is this and that—be sure to include why it's great
        </label>
 
        <label class="radio">
          <input type="radio" name="optionsRadios" id="optionsRadios1"         value="option1" checked>
          Option one is this and that—be sure to include why it's great
        </label>
        <label class="radio">
          <input type="radio" name="optionsRadios" id="optionsRadios2" value="option2">
          Option two can be something else and selecting it will deselect option one
        </label>        
        
#### dropdown

+ create a dropdown list   


        <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu">
          <li><a tabindex="-1" href="#">Action</a></li>
          <li><a tabindex="-1" href="#">Another action</a></li>
          <li><a tabindex="-1" href="#">Something else here</a></li>
          <li class="divider"></li>
          <li><a tabindex="-1" href="#">Separated link</a></li>
        </ul>
        
+ link it with a button/link 

        <div class="btn-group">
          <a class="btn dropdown-toggle" data-toggle="dropdown" href="#">
            Action
            <span class="caret"></span>
          </a>
          <ul class="dropdown-menu">
            <!-- dropdown menu links -->
          </ul>
        </div>
document.getElementsByTagName("select")[0].addEventListener("change", function() {
	location.replace(`/website/force/${document.getElementsByTagName("select")[0].selectedIndex + 1}`)
})
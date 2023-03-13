// header shrinks
const navigation = document.getElementById("navigation");
const logo = document.getElementById("logo");

window.addEventListener("scroll", () => {
	if (window.pageYOffset > 100) {
		navigation.classList =
			"navbar fixed-top d-flex justify-content-between navbar-expand-lg navbar-light smaller";
		logo.classList = "d-inline-block header-logo align-top smaller";
		logo.src = "./assets/logomenor.png";
	} else {
		navigation.classList =
			"navbar fixed-top d-flex justify-content-between navbar-expand-lg navbar-light";
		logo.classList = "d-inline-block header-logo align-top";
		logo.src = "./assets/logo.png";
	}
});

// header burger
const burger = document.getElementById("burger-container");
const nav = document.getElementById("menu-links");

function toggleMenu() {
	nav.classList.toggle("show");
	burger.classList.toggle("on");
	console.log("MENU!!!");
}

burger.addEventListener("click", toggleMenu);

// transitions
const observer = new IntersectionObserver((entries) => {
	entries.forEach((entry) => {
		console.log(entry);
		if (entry.isIntersecting) {
			entry.target.classList.add("show");
		}
	});
});

const hiddenElements = document.querySelectorAll(".hidden");
hiddenElements.forEach((el) => observer.observe(el));

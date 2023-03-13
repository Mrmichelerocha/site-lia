// Banners

const bannerContainer = document.getElementById("banner-container");
const banners = document.getElementsByClassName("banner");
const bannerIndicators = document.getElementsByClassName(
	"banner-indicator-circle"
);

function checkBanner() {
	let currentActive;
	for (const banner of banners) {
		if (banner.classList.contains("active")) {
			currentActive = banner.id[9];
		}
	}
	// console.log(`O banner ${currentActive} está ativo no momento.`);
	return currentActive;
}

for (const indicator of bannerIndicators) {
	indicator.addEventListener("click", (event) => {
		let clickedIndicator = event.currentTarget;
		let clickedIndicatorId = event.currentTarget.id[2];
		// clickedIndicatorId.replace("bn", "");
		let translateValue = (clickedIndicatorId - 1) * -100;

		// console.log(clickedIndicatorId);
		// console.log(clickedIndicatorId - 1);
		// console.log(translateValue);

		for (let i = 0; i < bannerIndicators.length; i++) {
			if (bannerIndicators[i].classList.contains("active")) {
				bannerIndicators[i].classList.toggle("active");
			}
		}

		clickedIndicator.classList.toggle("active");
		bannerContainer.style.transform = `translateX(${translateValue}vw)`;
		// bannerContainer.style.transform = `translateX(${translateValue})`;

		// banners[checkBanner()-1].toggle("active");

		for (const banner of banners) {
			if (banner.classList.contains("active")) {
				banner.classList.toggle("active");
			}
			if (banner.id.includes(clickedIndicatorId)) {
				banner.classList.toggle("active");
				// console.log(`Banner ${clickedIndicatorId} ativado!`);
			}
		}
		// a classe active do banner só serve pra localização dos botões esquerda direita
	});
}

function maxLeft() {
	// console.log("já tá no primeiro banner!");
	bannerContainer.style.transform = `translateX(10vw)`;
	setTimeout(function () {
		bannerContainer.style.transform = `translateX(0)`;
	}, 100);
}

function maxRight() {
	// console.log("já tá no ultimo banner!");
	bannerContainer.style.transform = `translateX(-210vw)`;
	setTimeout(function () {
		bannerContainer.style.transform = `translateX(-200vw)`;
	}, 100);
}

const leftButton = document.getElementById("left-button");
const rightButton = document.getElementById("right-button");

leftButton.addEventListener("click", (event) => {
	console.log("clicou no esquerdo");
	if (checkBanner() != 1) bannerIndicators[checkBanner() - 2].click();
	else maxLeft();
});

rightButton.addEventListener("click", (event) => {
	console.log("clicou no direito");
	if (checkBanner() != 3) bannerIndicators[checkBanner()].click();
	else maxRight();
});

// Banner Swipe - Touchscreen
// This section credits: https://www.kirupa.com/html5/detecting_touch_swipe_gestures.htm

const bannerSection = document.getElementById("intro");

bannerSection.addEventListener("touchstart", startTouch, false);
bannerSection.addEventListener("touchmove", moveTouch, false);

// Swipe Up / Down / Left / Right
var initialX = null;
var initialY = null;

function startTouch(e) {
	initialX = e.touches[0].clientX;
	initialY = e.touches[0].clientY;
}

function moveTouch(e) {
	if (initialX === null) {
		return;
	}

	if (initialY === null) {
		return;
	}

	var currentX = e.touches[0].clientX;
	var currentY = e.touches[0].clientY;

	var diffX = initialX - currentX;
	var diffY = initialY - currentY;

	if (Math.abs(diffX) > Math.abs(diffY)) {
		// sliding horizontally
		if (diffX > 0) {
			// swiped left
			rightButton.click();
		} else {
			// swiped right
			leftButton.click();
		}
	} else {
		// sliding vertically
		if (diffY > 0) {
			// swiped up
			console.log("swiped up");
		} else {
			// swiped down
			console.log("swiped down");
		}
	}

	initialX = null;
	initialY = null;

	e.preventDefault();
}

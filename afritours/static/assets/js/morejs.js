  // Get references to the necessary elements
  const popupTriggerElements = document.querySelectorAll('.popup-trigger');
  const overlayElement = document.querySelector('.overlay');
  const enlargedImageElement = overlayElement.querySelector('img');

  // Add event listeners to each image
  popupTriggerElements.forEach(function (triggerElement) {
    triggerElement.addEventListener('click', function () {
      const imageSource = this.getAttribute('src');
      enlargedImageElement.setAttribute('src', imageSource);
      overlayElement.style.display = 'block';
    });
  });

  // Add event listener to close the overlay when clicked outside the image
  overlayElement.addEventListener('click', function (event) {
    if (event.target === this) {
      overlayElement.style.display = 'none';
    }
  });
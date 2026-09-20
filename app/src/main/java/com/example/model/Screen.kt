package com.example.model

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ContactSupport
import androidx.compose.material.icons.filled.Calculate
import androidx.compose.material.icons.filled.CalendarMonth
import androidx.compose.material.icons.filled.Description
import androidx.compose.material.icons.filled.Favorite
import androidx.compose.material.icons.filled.Gavel
import androidx.compose.material.icons.filled.Home
import androidx.compose.material.icons.filled.Info
import androidx.compose.material.icons.filled.LocalOffer
import androidx.compose.material.icons.filled.Percent
import androidx.compose.material.icons.filled.PrivacyTip
import androidx.compose.runtime.saveable.Saver
import androidx.compose.ui.graphics.vector.ImageVector

sealed class Screen(
  val route: String,
  val title: String,
  val metaTitle: String,
  val metaDescription: String,
  val icon: ImageVector,
  val isTool: Boolean = false
) {
  object Home : Screen(
    route = "home",
    title = "MY USEFUL TOOLS",
    metaTitle = "MY USEFUL TOOLS - Free Online Calculators & Utilities",
    metaDescription = "Free, simple and easy-to-use online calculators and tools. Fast, lightweight and private.",
    icon = Icons.Default.Home
  )

  object AgeCalculator : Screen(
    route = "age-calculator",
    title = "Age Calculator",
    metaTitle = "Age Calculator - Exact Years, Months & Days | MY USEFUL TOOLS",
    metaDescription = "Calculate your exact age in years, months, and days. Find your next birthday countdown and fun timeline facts.",
    icon = Icons.Default.CalendarMonth,
    isTool = true
  )

  object EmiCalculator : Screen(
    route = "emi-calculator",
    title = "EMI Calculator",
    metaTitle = "EMI Calculator - Loan Monthly Installment & Interest | MY USEFUL TOOLS",
    metaDescription = "Calculate your monthly loan EMI, total interest payable, and total loan payment with interest breakdown.",
    icon = Icons.Default.Calculate,
    isTool = true
  )

  object PercentageCalculator : Screen(
    route = "percentage-calculator",
    title = "Percentage Calculator",
    metaTitle = "Percentage Calculator - Percent Increase, Decrease & Value | MY USEFUL TOOLS",
    metaDescription = "Calculate percentages, percentage increase or decrease, and proportional values with ease.",
    icon = Icons.Default.Percent,
    isTool = true
  )

  object DiscountCalculator : Screen(
    route = "discount-calculator",
    title = "Discount Calculator",
    metaTitle = "Discount Calculator - Sale Price & Savings | MY USEFUL TOOLS",
    metaDescription = "Calculate final sale price, discount amount saved, and optional sales tax quickly.",
    icon = Icons.Default.LocalOffer,
    isTool = true
  )

  object BmiCalculator : Screen(
    route = "bmi-calculator",
    title = "BMI Calculator",
    metaTitle = "BMI Calculator - Body Mass Index & Healthy Weight | MY USEFUL TOOLS",
    metaDescription = "Calculate your Body Mass Index (BMI), view your BMI category, and find your healthy weight range.",
    icon = Icons.Default.Favorite,
    isTool = true
  )

  object AboutUs : Screen(
    route = "about-us",
    title = "About Us",
    metaTitle = "About Us - Free Fast Utilities | MY USEFUL TOOLS",
    metaDescription = "Learn about MY USEFUL TOOLS, our mission to provide free, privacy-first, and lightweight calculation tools.",
    icon = Icons.Default.Info
  )

  object ContactUs : Screen(
    route = "contact-us",
    title = "Contact Us",
    metaTitle = "Contact Us - Feedback & Support | MY USEFUL TOOLS",
    metaDescription = "Get in touch with the MY USEFUL TOOLS team for questions, tool requests, or feedback.",
    icon = Icons.AutoMirrored.Filled.ContactSupport
  )

  object PrivacyPolicy : Screen(
    route = "privacy-policy",
    title = "Privacy Policy",
    metaTitle = "Privacy Policy | MY USEFUL TOOLS",
    metaDescription = "Read our transparent privacy policy. No registration, no tracking, and 100% browser-side processing.",
    icon = Icons.Default.PrivacyTip
  )

  object TermsConditions : Screen(
    route = "terms-conditions",
    title = "Terms & Conditions",
    metaTitle = "Terms & Conditions | MY USEFUL TOOLS",
    metaDescription = "Terms and conditions of use for MY USEFUL TOOLS free online utility website.",
    icon = Icons.Default.Gavel
  )

  object Disclaimer : Screen(
    route = "disclaimer",
    title = "Disclaimer",
    metaTitle = "Disclaimer - Financial & Health Information | MY USEFUL TOOLS",
    metaDescription = "Important disclaimer regarding calculator results, financial estimations, and health indicators.",
    icon = Icons.Default.Description
  )

  companion object {
    val allTools = listOf(
      AgeCalculator,
      EmiCalculator,
      PercentageCalculator,
      DiscountCalculator,
      BmiCalculator
    )

    val legalPages = listOf(
      AboutUs,
      ContactUs,
      PrivacyPolicy,
      TermsConditions,
      Disclaimer
    )

    val allScreens: List<Screen> by lazy {
      listOf(Home) + allTools + legalPages
    }

    fun fromRoute(route: String?): Screen {
      return allScreens.find { it.route == route } ?: Home
    }

    val Saver: Saver<Screen, String> = Saver(
      save = { it.route },
      restore = { fromRoute(it) }
    )
  }
}

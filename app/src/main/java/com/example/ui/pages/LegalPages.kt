package com.example.ui.pages

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.Send
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.filled.ContactSupport
import androidx.compose.material.icons.filled.Description
import androidx.compose.material.icons.filled.Email
import androidx.compose.material.icons.filled.Gavel
import androidx.compose.material.icons.filled.Info
import androidx.compose.material.icons.filled.PrivacyTip
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.model.Screen
import com.example.ui.components.AdSensePlaceholder
import com.example.ui.theme.Emerald600

@Composable
fun LegalPageScreen(screen: Screen, modifier: Modifier = Modifier) {
  Column(
    modifier = modifier
      .fillMaxWidth()
      .padding(16.dp)
  ) {
    // Header
    Row(verticalAlignment = Alignment.CenterVertically) {
      Icon(
        imageVector = screen.icon,
        contentDescription = null,
        tint = MaterialTheme.colorScheme.primary,
        modifier = Modifier.size(28.dp)
      )
      Spacer(modifier = Modifier.width(10.dp))
      Text(
        text = screen.title,
        style = MaterialTheme.typography.headlineMedium,
        fontWeight = FontWeight.Bold,
        color = MaterialTheme.colorScheme.onBackground
      )
    }

    Text(
      text = screen.metaDescription,
      style = MaterialTheme.typography.bodyMedium,
      color = MaterialTheme.colorScheme.onSurfaceVariant,
      modifier = Modifier.padding(top = 6.dp, bottom = 12.dp)
    )

    AdSensePlaceholder(slotLabel = "AdSense Responsive Slot - Legal Page Top")

    when (screen) {
      Screen.AboutUs -> AboutUsContent()
      Screen.ContactUs -> ContactUsContent()
      Screen.PrivacyPolicy -> PrivacyPolicyContent()
      Screen.TermsConditions -> TermsConditionsContent()
      Screen.Disclaimer -> DisclaimerContent()
      else -> {}
    }

    Spacer(modifier = Modifier.height(16.dp))
    AdSensePlaceholder(slotLabel = "AdSense Responsive Slot - Legal Page Bottom")
  }
}

@Composable
private fun AboutUsContent() {
  Card(
    modifier = Modifier.fillMaxWidth(),
    colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface),
    shape = RoundedCornerShape(16.dp),
    elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
  ) {
    Column(modifier = Modifier.padding(20.dp)) {
      Text(
        text = "Welcome to MY USEFUL TOOLS",
        style = MaterialTheme.typography.titleMedium,
        fontWeight = FontWeight.Bold,
        color = MaterialTheme.colorScheme.primary
      )
      Spacer(modifier = Modifier.height(8.dp))
      Text(
        text = "MY USEFUL TOOLS is an open, completely free collection of high-performance online utility calculators designed for everyday life, finance, health, and education.\n\n" +
            "Our philosophy is centered on speed, privacy, and simplicity:\n\n" +
            "• 100% Free Forever: No hidden subscriptions, no trial periods, and no credit cards required.\n" +
            "• Zero Registration: Use every tool instantly without signing up or providing personal logins.\n" +
            "• Client-Side Processing: Every calculation runs directly on your device inside your browser or app. Your private numbers are never sent to external tracking servers.\n" +
            "• Fast & Mobile-Optimized: Built to load in milliseconds on mobile devices, tablets, and desktop computers alike.",
        style = MaterialTheme.typography.bodyMedium,
        color = MaterialTheme.colorScheme.onSurface,
        lineHeight = 22.sp
      )
    }
  }
}

@Composable
private fun ContactUsContent() {
  var name by remember { mutableStateOf("") }
  var email by remember { mutableStateOf("") }
  var message by remember { mutableStateOf("") }
  var submitted by remember { mutableStateOf(false) }
  var error by remember { mutableStateOf<String?>(null) }

  Card(
    modifier = Modifier.fillMaxWidth(),
    colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface),
    shape = RoundedCornerShape(16.dp),
    elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
  ) {
    Column(modifier = Modifier.padding(20.dp)) {
      Text(
        text = "Send Us a Message",
        style = MaterialTheme.typography.titleMedium,
        fontWeight = FontWeight.Bold,
        color = MaterialTheme.colorScheme.primary
      )
      Spacer(modifier = Modifier.height(6.dp))
      Text(
        text = "Have feedback, question, or want to suggest a new tool? We'd love to hear from you.",
        style = MaterialTheme.typography.bodyMedium,
        color = MaterialTheme.colorScheme.onSurfaceVariant
      )

      Spacer(modifier = Modifier.height(16.dp))

      if (submitted) {
        Box(
          modifier = Modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(12.dp))
            .background(Emerald600.copy(alpha = 0.15f))
            .padding(16.dp),
          contentAlignment = Alignment.Center
        ) {
          Column(horizontalAlignment = Alignment.CenterHorizontally) {
            Icon(
              imageVector = Icons.Default.CheckCircle,
              contentDescription = null,
              tint = Emerald600,
              modifier = Modifier.size(36.dp)
            )
            Spacer(modifier = Modifier.height(8.dp))
            Text(
              text = "Thank You, $name!",
              style = MaterialTheme.typography.titleMedium,
              fontWeight = FontWeight.Bold,
              color = Emerald600
            )
            Text(
              text = "Your message has been received. Our team will review your inquiry shortly.",
              style = MaterialTheme.typography.bodySmall,
              color = MaterialTheme.colorScheme.onSurface,
              modifier = Modifier.padding(top = 4.dp)
            )
          }
        }
      } else {
        OutlinedTextField(
          value = name,
          onValueChange = { name = it },
          label = { Text("Your Name") },
          placeholder = { Text("John Doe") },
          singleLine = true,
          modifier = Modifier
            .fillMaxWidth()
            .testTag("contact_name_input")
        )

        Spacer(modifier = Modifier.height(12.dp))

        OutlinedTextField(
          value = email,
          onValueChange = { email = it },
          label = { Text("Email Address") },
          placeholder = { Text("name@example.com") },
          keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Email),
          singleLine = true,
          modifier = Modifier
            .fillMaxWidth()
            .testTag("contact_email_input")
        )

        Spacer(modifier = Modifier.height(12.dp))

        OutlinedTextField(
          value = message,
          onValueChange = { message = it },
          label = { Text("Message / Suggestion") },
          placeholder = { Text("Write your comments here...") },
          minLines = 4,
          maxLines = 6,
          modifier = Modifier
            .fillMaxWidth()
            .testTag("contact_message_input")
        )

        if (error != null) {
          Spacer(modifier = Modifier.height(8.dp))
          Text(
            text = error ?: "",
            color = MaterialTheme.colorScheme.error,
            style = MaterialTheme.typography.bodySmall
          )
        }

        Spacer(modifier = Modifier.height(16.dp))

        Button(
          onClick = {
            if (name.isBlank() || email.isBlank() || message.isBlank()) {
              error = "Please fill in all fields before sending."
            } else if (!email.contains("@") || !email.contains(".")) {
              error = "Please provide a valid email address."
            } else {
              error = null
              submitted = true
            }
          },
          modifier = Modifier
            .fillMaxWidth()
            .height(48.dp)
            .testTag("submit_contact_button")
        ) {
          Icon(Icons.AutoMirrored.Filled.Send, contentDescription = null, modifier = Modifier.size(18.dp))
          Spacer(modifier = Modifier.width(8.dp))
          Text("Send Feedback")
        }
      }
    }
  }
}

@Composable
private fun PrivacyPolicyContent() {
  Card(
    modifier = Modifier.fillMaxWidth(),
    colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface),
    shape = RoundedCornerShape(16.dp),
    elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
  ) {
    Column(modifier = Modifier.padding(20.dp)) {
      Text(
        text = "Privacy Policy & AdSense Disclosure",
        style = MaterialTheme.typography.titleMedium,
        fontWeight = FontWeight.Bold,
        color = MaterialTheme.colorScheme.primary
      )
      Spacer(modifier = Modifier.height(8.dp))
      Text(
        text = "Last updated: 2026\n\n" +
            "1. Information We Do Not Collect\n" +
            "MY USEFUL TOOLS does not require account creation, logins, or personal details. Numbers entered into calculators (such as dates of birth, loan amounts, weight, or prices) remain strictly local on your device and are never transmitted to our servers.\n\n" +
            "2. Google AdSense & Third-Party Cookies\n" +
            "We may display third-party advertisements served by Google AdSense to support the free operation of this service. Google, as a third-party vendor, uses cookies to serve ads based on prior visits to our website or other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visit to our sites and/or other sites on the Internet. Users may opt out of personalized advertising by visiting Google Ads Settings.\n\n" +
            "3. Compliance with Privacy Regulations (GDPR / CCPA)\n" +
            "We respect international privacy frameworks. Because we do not store personal profiles, your rights to privacy, data minimization, and protection are built into our architecture by design.\n\n" +
            "4. Contact Information\n" +
            "For inquiries regarding this privacy policy, please reach out via our Contact Us page.",
        style = MaterialTheme.typography.bodyMedium,
        color = MaterialTheme.colorScheme.onSurface,
        lineHeight = 22.sp
      )
    }
  }
}

@Composable
private fun TermsConditionsContent() {
  Card(
    modifier = Modifier.fillMaxWidth(),
    colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface),
    shape = RoundedCornerShape(16.dp),
    elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
  ) {
    Column(modifier = Modifier.padding(20.dp)) {
      Text(
        text = "Terms & Conditions of Use",
        style = MaterialTheme.typography.titleMedium,
        fontWeight = FontWeight.Bold,
        color = MaterialTheme.colorScheme.primary
      )
      Spacer(modifier = Modifier.height(8.dp))
      Text(
        text = "1. Acceptance of Terms\n" +
            "By accessing and using MY USEFUL TOOLS, you agree to comply with and be bound by these terms.\n\n" +
            "2. Permitted Use\n" +
            "All calculators, tools, and content on this service are provided free of charge for personal and non-commercial educational use.\n\n" +
            "3. Intellectual Property\n" +
            "The branding, layout, interfaces, and code of MY USEFUL TOOLS are protected by applicable copyright and intellectual property laws.\n\n" +
            "4. Limitation of Liability\n" +
            "In no event shall MY USEFUL TOOLS or its contributors be liable for any damages arising out of the use or inability to use the tools on this website.",
        style = MaterialTheme.typography.bodyMedium,
        color = MaterialTheme.colorScheme.onSurface,
        lineHeight = 22.sp
      )
    }
  }
}

@Composable
private fun DisclaimerContent() {
  Card(
    modifier = Modifier.fillMaxWidth(),
    colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface),
    shape = RoundedCornerShape(16.dp),
    elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
  ) {
    Column(modifier = Modifier.padding(20.dp)) {
      Text(
        text = "General, Financial & Health Disclaimer",
        style = MaterialTheme.typography.titleMedium,
        fontWeight = FontWeight.Bold,
        color = MaterialTheme.colorScheme.error
      )
      Spacer(modifier = Modifier.height(8.dp))
      Text(
        text = "1. Informational Purposes Only\n" +
            "All information, calculations, and estimates generated by MY USEFUL TOOLS are provided on an 'as is' basis for general informational and educational purposes only.\n\n" +
            "2. Financial Disclaimer (EMI & Discount Calculators)\n" +
            "Calculations regarding loans, interest rates, equated monthly installments (EMI), and discounts are theoretical models. Actual loan terms, processing fees, compounding cycles, and taxes vary by lending institution, bank, or retailer. Always consult a certified financial advisor or official lender before making significant financial commitments.\n\n" +
            "3. Health & Medical Disclaimer (BMI Calculator)\n" +
            "Body Mass Index (BMI) is a screening metric and does not diagnose body fatness or the health of an individual. BMI does not account for muscle mass, bone density, ethnicity, or clinical conditions. This calculator is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or qualified healthcare provider.\n\n" +
            "4. No Guarantee of Accuracy\n" +
            "While we strive to ensure all mathematical formulas are correct, we make no warranties or representations of any kind regarding accuracy, completeness, or reliability.",
        style = MaterialTheme.typography.bodyMedium,
        color = MaterialTheme.colorScheme.onSurface,
        lineHeight = 22.sp
      )
    }
  }
}
